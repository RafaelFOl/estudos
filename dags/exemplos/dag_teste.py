import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkubernetesOperator

with DAG(
    dag_id="example_python_operator",
    schedule_interval=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    
    taxi_task_select = SparkubernetesOperator(
        task_id="taxi_task_select",
        namespace='spark',
        application_file='taxi-spark-app.yaml',
        kubernetes_conn_id='k8s')
    
taxi_task_select