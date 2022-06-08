import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from kubernetes.client import models as k8s

with DAG(
    dag_id="example_python_operator",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 6, 8, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    
    taxi_task_select = KubernetesPodOperator(
        namespace='spark',
        image="senior2017/taxi-pipe:1.8",
        name='taxi_task_select',
        is_delete_operator_pod=True,
        in_cluster=True,
        task_id="taxi_task_select",
        get_logs=True,
        pod_template_file='taxi-spark-app.yaml'
)
    
taxi_task_select