import pendulum

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

with DAG(
    dag_id="example_python_operator",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 6, 8, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    
    taxi_task_select = KubernetesPodOperator(
        namespace='spark',
        image="senior2017/taxi-pipe:1.14",
        name='taxi_task_select',
        is_delete_operator_pod=False,
        in_cluster=True,
        task_id="taxi_task_select",
        get_logs=True,
        cmds=['./run.sh'])
    
taxi_task_select