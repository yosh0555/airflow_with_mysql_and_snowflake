from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'yosh0555',
    'start_date': datetime(2024, 3, 27),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define a DAG
mysqltosfdag = DAG('mysql_to_snowflake_poc',
        default_args=default_args,
        description='Extracting mysql dept table data, processing this data and storing it into snowflake',
        start_date=datetime(2024, 3, 27),
        schedule_interval='*/5 * * * *',
        catchup=True
)

spark_job = SparkSubmitOperator(
        task_id = 'spark_job_task',
        application = '~/spark.py',
        conn_id = 'connect_spark',
        verbose = False,
        jars = '~/mysql-connector-java-8.0.11.jar,~/snowflake-jdbc-3.14.4.jar,~/snowflake-ingest-sdk-2.0.2.jar,~/spark-snowflake_2.12-2.11.3-spark_3.1.jar',
        dag = mysqltosfdag
)
