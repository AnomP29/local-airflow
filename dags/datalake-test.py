from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

import os
from pathlib import Path

# os.chdir('/opt/airflow/dags/repo/dags')
# airflow_home = Path(os.environ.get("AIRFLOW_HOME", "/opt/airflow/dags/repo/dags/spark_job"))
# sp_dir = airflow_home / "spark_job"
spark_dir = Path('/opt/airflow/dags/repo/dags')

default_args = {
    'owner': 'anomp',
    'start_date': datetime(2025, 3, 16),
    'retries': 1,
    'catchup': False
}

with DAG(
    'Datalake-Test',
    default_args = default_args,
    schedule_interval=None

) as dag:
    start = EmptyOperator(task_id="start")
    spark_test_1 = EmptyOperator(task_id="spark_test_1")
    # PythonOperator(
    #     task_id='spark_test_1',
    #     provide_context=True,
    #     python_callable=spark_builder
    #     )
    
    spark_test_2 = BashOperator(
        task_id='spark_submit_test',
        bash_command=f"""
        spark-submit \
        --jars /opt/spark/jars/hadoop-aws-3.3.2.jar,/opt/spark/jars/aws-java-sdk-bundle-1.11.901.jar \
        --properties-file {spark_dir}/spark-job/spark-defaults.conf \
        {spark_dir}/spark-job/sp-job-01.py 2>&1
        """
    )    
    task1 = EmptyOperator(task_id="task1")

    end = EmptyOperator(task_id="end")

    start >> spark_test_2 >> end

        # --master spark://172.18.0.6:7077 \
        # --conf spark.hadoop.fs.s3a.endpoint=http://172.18.0.2:9000 \
        # --conf spark.hadoop.fs.s3a.access.key=minioadmin \
        # --conf spark.hadoop.fs.s3a.secret.key=minioadmin \
        # --conf spark.hadoop.fs.s3a.path.style.access=true \
        # --conf spark.hadoop.fs.s3a.connection.ssl.enabled=false \
        # --conf spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem \
        # --conf spark.sql.catalogImplementation=hive \
        # --conf hive.metastore.uris=thrift://172.18.0.4:9083 \
