import pendulum

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import task,dag


def _extract(ds):
    print(ds)

@task.python
def _xxcom():
    return {"key":'ola',"value":"mundo"}

with DAG(
    dag_id="example_python_operator",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 6, 8, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    


    ds_teste = PythonOperator(
        task_id="ds_teste",
        python_callable=_extract
    )
    _xxcom()>>ds_teste


    


#taxi_task_select