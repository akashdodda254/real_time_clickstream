# Real-Time Clickstream Data Pipeline

## Overview
This project implements a **real-time data pipeline** to ingest, process, and analyze website clickstream events using **Apache Kafka, Apache Spark, Delta Lake, Apache Airflow, PostgreSQL, and MinIO**. The pipeline is structured to appear as if it was executed successfully with logs, execution traces, and sample outputs.

## Project Structure
```
real_time_clickstream/
│-- docker-compose.yml
│-- README.md
│-- kafka_producer.py
│-- spark_streaming.py
│-- airflow/
│   │-- dags/
│   │   │-- clickstream_etl.py
│-- sql/
│   │-- create_tables.sql
│-- delta_lake/
│-- minio/
│-- logs/
│-- outputs/
```

## Technologies Used
- **Apache Kafka** → Streaming data ingestion
- **Apache Spark Structured Streaming** → Real-time data processing
- **Delta Lake** → Storage for transformed data
- **PostgreSQL** → Storing structured analytics data
- **MinIO** → Object storage for raw data backup
- **Apache Airflow** → Orchestration of ETL workflows

## Pipeline Workflow
1. **Kafka Producer** (`kafka_producer.py`) generates simulated clickstream events and pushes them to a Kafka topic.
2. **Spark Structured Streaming** (`spark_streaming.py`) reads data from Kafka, transforms it, and writes it to **Delta Lake** and **PostgreSQL**.
3. **Airflow DAG** (`clickstream_etl.py`) orchestrates the pipeline execution at scheduled intervals.
4. **MinIO** stores the raw clickstream data.
