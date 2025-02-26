from datetime import timedelta
import os
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
import time

default_args = {
    'owner': 'AnmP',
    'retries': 3,
    'start_date': datetime(2024, 0o3, 0o4),
    'catchup': False,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'dbt_airflow_01',
    default_args = default_args,
    schedule_interval=None,
    template_searchpath='/opt/airflow/dags/repo/dags/dbt/'
)

dbt_task = KubernetesPodOperator(
    task_id='dbt_airflow_pod',
    name='dbt_airflow_pod',
    namespace='dbt-local',
    image='anompu/dbt_dev:v1.0.0', 
    image_pull_policy='Always',
    service_account_name="dbt-local", 
    cluster_context="docker-desktop",
    cmds=['dbt'],
    arguments=['run', '--profiles-dir', '/dbt/profiles', '--fail-fast', '-m', 'customer_sales'],
    get_logs=True,
    dag=dag,
    is_delete_operator_pod=True
)

dbt_task
