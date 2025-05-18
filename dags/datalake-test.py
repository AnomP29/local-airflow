from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago


import pandas as pd
import numpy as np
import psycopg2
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

default_args = {
    'owner': 'anomp',
    'start_date': datetime(2025, 3, 16),
    'retries': 1,
    'catchup': False
}

with DAG(
    'Datalake Test',
    default_args = default_args,
    schedule_interval=None
) as dag:
    start = EmptyOperator(task_id="start")
    task1 = EmptyOperator(task_id="task1")
    end = EmptyOperator(task_id="end")

    start >> task1 >> end
