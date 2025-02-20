from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("ClickstreamProcessor") \
    .getOrCreate()

schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("url", StringType(), True),
    StructField("timestamp", DoubleType(), True)
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "clickstream") \
    .load()

parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

query = parsed_df.writeStream \
    .format("console") \
    .start()

query.awaitTermination()