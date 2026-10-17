from datetime import datetime  # CHANGED: days_ago hata diya

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator  # CHANGED


dag = DAG(
    'depends_on_past',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 21 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False,
)

# Define tasks
task_a = PythonOperator(
    task_id="task_a",
    python_callable=lambda: print("Executing Task A"),
    dag=dag,
)

# first time make it fail, second time make it good, but it should fail bcz of depends_on_past condition.
task_b = PythonOperator(
    task_id="task_b",
    python_callable=lambda: raise_exception("Failure in Query c"),
    depends_on_past=True,
    dag=dag,
)

# this is for success task
# task_b = PythonOperator(
#     task_id="task_b",
#     python_callable=lambda: print("Executing Task B"),
#     depends_on_past=True,
#     dag=dag,
# )


# Connect tasks
task_a >> task_b