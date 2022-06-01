import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    dag_id="example_python_operator",
    schedule_interval=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    def print_array():
        import numpy as np
        """Print Numpy array."""
        a = np.arange(15).reshape(3, 5)
        print(a)
        return a

    run_this = PythonOperator(
        task_id="print_the_context",
        python_callable=print_array,
    )
run_this