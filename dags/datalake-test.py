from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

import os
from pathlib import Path

# os.chdir('/opt/airflow/dags/repo/dags')
airflow_home = Path(os.environ.get("AIRFLOW_HOME", "/opt/airflow/dags/repo/dags/spark_job"))
# sp_dir = airflow_home / "spark_job"

default_args = {
    'owner': 'anomp',
    'start_date': datetime(2025, 3, 16),
    'retries': 1,
    'catchup': False
}


def spark_builder():
    print('a')
    builder = SparkSession.builder \
        .appName("MyApp") \
        .master("spark://172.18.0.6:7077") \
        .enableHiveSupport() \
        .config("spark.hadoop.fs.s3a.endpoint", "http://172.18.0.4:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.addressing.style", "path") \
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    spark = builder.getOrCreate()
    spark.sql("SHOW TABLES").show()
    return spark.sql("SHOW TABLES").show()



with DAG(
    'Datalake-Test',
    default_args = default_args,
    schedule_interval=None

) as dag:
    start = EmptyOperator(task_id="start")
    spark_test_1 = PythonOperator(
        task_id='spark_test_1',
        provide_context=True,
        python_callable=spark_builder
        )
    
    spark_test_2 = BashOperator(
        task_id='spark_submit_test',
        bash_command="""
        spark-submit \
        --master spark://172.18.0.6:7077 \
        --conf spark.hadoop.fs.s3a.endpoint=http://172.18.0.4:9000 \
        --conf spark.hadoop.fs.s3a.access.key=minioadmin \
        --conf spark.hadoop.fs.s3a.secret.key=minioadmin \
        --conf spark.hadoop.fs.s3a.path.style.access=true \
        --conf spark.hadoop.fs.s3a.connection.ssl.enabled=false \
        --conf spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem \
        {airflow_home}/sp-job-01.py
        """.format(airflow_home = airflow_home)
    )
    
    task1 = EmptyOperator(task_id="task1")

    end = EmptyOperator(task_id="end")

    start >> spark_test_2 >> end
