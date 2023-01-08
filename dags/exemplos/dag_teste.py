import pendulum

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import task, dag


with DAG(
    dag_id="example_python_operator",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 6, 8, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    
    taxi_task_select = KubernetesPodOperator(
        namespace='spark-operator',
        image="rroliveira/taxi-pipe:1.10",
        name='taxi_task_select',
        is_delete_operator_pod=False,
        in_cluster=True,
        task_id="taxi_task_select",
        get_logs=True,    
        cmds=['/opt/spark/bin/spark-submit'],
         arguments=[ 
        '--master','k8s://https://10.96.0.1:443',
        '--name','spark-name1',
        '--conf', 'spark.kubernetes.namespace=spark-operator',
        '--conf', 'spark.kubernetes.allocation.batch.size=3',
        '--conf', 'spark.kubernetes.allocation.batch.delay=1',
        '--conf', 'spark.driver.cores=1',
        '--conf', 'spark.executor.cores=1',
        '--conf', 'spark.driver.memory=2192m',
        '--conf', 'spark.executor.memory=2192m',
        '--conf', 'spark.dynamicAllocation.enabled=true',
        '--conf', 'spark.dynamicAllocation.shuffleTracking.enabled=true',
        '--conf', 'spark.kubernetes.driver.container.image=rroliveira/taxi-pipe:1.10',
        '--conf', 'spark.kubernetes.executor.container.image=rroliveira/taxi-pipe:1.10',
        '--conf', 'spark.kubernetes.authenticate.driver.serviceAccountName=default',
        '--class' ,'org.apache.spark.examples.SparkPi',
        '--deploy-mode','cluster', 
        'local:///app/taxispark.py'
         ]
     )
    taxi_task_select