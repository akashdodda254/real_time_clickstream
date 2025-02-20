from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 20),
    'retries': 1
}

dag = DAG(
    dag_id='clickstream_etl',
    default_args=default_args,
    schedule_interval='@hourly'
)

task1 = BashOperator(
    task_id='extract_data',
    bash_command='python3 /opt/airflow/dags/spark_streaming.py',
    dag=dag
)
