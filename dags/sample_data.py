from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

import pandas as pd
import numpy as np
import psycopg2
import petl as etl
# import gspread
from ruamel.yaml import YAML


def toPostgres():
    df1 = pd.DataFrame(np.random.randint(1,10,size=(10, 3)))
    a = np.random.randint(1,10,size=(3, 3)).tolist()
    # a.tolist()
    df2 = pd.DataFrame(a, columns=('CustId', 'A', 'B'))
    df2['CustName'] = 'Customer_'
    df2['Customer'] = df2['CustName'] + df2['CustId'].astype(str)
    df2 = df2[['Customer', 'A', 'B']]    
    try:
        conn = psycopg2.connect(database = 'dbt_local_proj', host = '172.27.16.1', user = 'postgres', password = 'dataEngineer01')
        df2.to_sql('sample_data', con=conn, if_exists='append', index=False)
    except Exception as e:
        print(e)

default_args = {
    'owner': 'anomp',
    'start_date': days_ago(1),
    'catchup': False
}

dag = DAG(
    'Sample_data',
    default_args = default_args,
    schedule_interval='30 * * * *'
)

data_sample = PythonOperator(
    task_id='random_number_01',
    provide_context=True,
    python_callable=toPostgres,
    dag=dag,
)

data_sample
