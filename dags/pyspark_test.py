from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago


import pandas as pd
import numpy as np
import psycopg2
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
# import petl as etl
# import gspread
# from ruamel.yaml import YAML
# from sqlalchemy import create_engine

def pyspark01():
    spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial").config("spark.memory.offHeap.enabled","true").config("spark.memory.offHeap.size","10g").getOrCreate()
    df = spark.read.csv('../dags/repo/sample-data/car_price_dataset.csv',header=True,escape="\"")
    print(df.show())


default_args = {
    'owner': 'anomp',
    'start_date': datetime(2025, 2, 27),
    'retries': 1,
    'catchup': False
}

dag = DAG(
    'Spark_Tut',
    default_args = default_args,
    schedule_interval=None
)

spark_sample = PythonOperator(
    task_id='exmp-01',
    provide_context=True,
    python_callable=pyspark01,
    dag=dag,
)

spark_sample
