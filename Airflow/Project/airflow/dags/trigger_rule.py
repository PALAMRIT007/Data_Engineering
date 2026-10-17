from datetime import datetime  # CHANGED: days_ago hata diya

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator  # CHANGED
# CHANGED: DummyOperator import hata diya (use hi nahi ho raha tha, aur Airflow 3 mein hai bhi nahi)


dag = DAG(
    'trigger_rules',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 21 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False
)

# Define tasks
task_a = PythonOperator(
    task_id='task_a',
    python_callable=lambda: raise_exception("Failure in Query a"),
    dag=dag,
)

task_b = PythonOperator(
    task_id='task_b',
    python_callable=lambda: raise_exception("Failure in Query b"),
    dag=dag,
)

task_c = PythonOperator(
    task_id='task_c',
    python_callable=lambda: raise_exception("Failure in Query c"),
    dag=dag,
)

task_d = PythonOperator(
    task_id='task_d',
    python_callable=lambda: print("Executing Task D"),
    dag=dag,
    trigger_rule='all_failed',
)

task_e = PythonOperator(
    task_id='task_e',
    python_callable=lambda: print("Executing Task E"),
    dag=dag,
)

# Define task dependencies
task_a >> task_d
task_b >> task_d
task_c >> task_d
task_d >> task_e