from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

import pandas as pd
# import gspread


df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])
print(df)

default_args = {
    'owner': 'anomp',
    'start_date': datetime(2024, 0o3, 0o4),
    'catchup': False
}

dag = DAG(
    'Testing_1st_DAGS',
    default_args = default_args,
    schedule_interval=None
)

t1 = BashOperator(
    task_id = 'first_k8s',
    bash_command ='echo $var1_name && echo $var2_name',
    env={
        "var1_name": df.astype(str),
        "var2_name": "static value",
    },
    dag = dag
)


t2 = BashOperator(
    task_id = 'rvm',
    bash_command ='echo "Anm_Go ahead"',
    dag = dag
)

t1 >> t2
