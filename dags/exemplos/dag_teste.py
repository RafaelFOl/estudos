import pendulum

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.python import PythonOperator

def _extract(ds):
    print(ds)

def _xxcom():
    return {"key":'ola',"value":"mundo"}

with DAG(
    dag_id="example_python_operator",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 6, 8, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    
    taxi_task_select = KubernetesPodOperator(
        namespace='spark',
        image="rroliveira/taxi-pipe:1.0",
        name='taxi_task_select',
        is_delete_operator_pod=True,
        in_cluster=True,
        task_id="taxi_task_select",
        get_logs=True,    
        cmds=['/opt/spark/bin/spark-submit'],
         arguments=[ 
        '--master','k8s://https://10.96.0.1:443',
        '--name','spark-name1',
        '--conf', 'spark.kubernetes.namespace=spark',
        '--conf', 'spark.kubernetes.allocation.batch.size=3',
        '--conf', 'spark.kubernetes.allocation.batch.delay=1',
        '--conf', 'spark.driver.cores=1',
        '--conf', 'spark.executor.cores=1',
        '--conf', 'spark.driver.memory=2192m',
        '--conf', 'spark.executor.memory=2192m',
        '--conf', 'spark.dynamicAllocation.enabled=true',
        '--conf', 'spark.dynamicAllocation.shuffleTracking.enabled=true',
        '--conf', 'spark.kubernetes.driver.container.image=rroliveira/taxi-pipe:1.0',
        '--conf', 'spark.kubernetes.executor.container.image=rroliveira/taxi-pipe:1.0',
        '--conf', 'spark.kubernetes.authenticate.driver.serviceAccountName=default',
        '--class' ,'org.apache.spark.examples.SparkPi',
        '--deploy-mode','cluster', 
        'local:///app/taxispark.py'
         ]
     )
    ds_teste = PythonOperator(
        task_id="ds_teste",
        python_callable=_extract
    )

    com_teste = PythonOperator(
        task_id="com_teste",
        python_callable=_xxcom
    )


    
ds_teste
com_teste
taxi_task_select