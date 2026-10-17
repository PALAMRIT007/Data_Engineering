from datetime import datetime  # CHANGED: days_ago hata diya

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator  # CHANGED
from airflow.providers.standard.operators.latest_only import LatestOnlyOperator  # CHANGED
from airflow.providers.smtp.operators.smtp import EmailOperator  # CHANGED

def notify_success():
    print('UK Sales table to Profit table Load Completed')





dag = DAG(
    'LatestOnly',
    start_date=datetime(2026, 10, 14),  # CHANGED: days_ago(3) ki jagah fixed date (aaj 17 se 3 din pehle)
    schedule='0 2 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=True,
)

# Define tasks
task_a = PythonOperator(
    task_id='task_a',
    python_callable=lambda: print("Executing Task A"),
    dag=dag,
)

task_b = PythonOperator(
    task_id='task_b',
    python_callable=lambda: print("Executing Task B"),
    dag=dag,
)

# Send email based on success
# send_email_completed = EmailOperator(
#     task_id="send_email_completed",
#     to="{{ var.value.get('support_email') }}",
#     subject="UK Sales Data Load - Successful",
#     html_content="UK Sales Data Load Completed Successfully.",
#     dag=dag,
# )

send_email_completed = PythonOperator(
    task_id='send_email',
    python_callable=notify_success,
    dag=dag,
)

# Send email based on failure
send_email_failed = EmailOperator(
    task_id="send_email_failed",
    to="{{ var.value.get('support_email') }}",
    subject="UK Sales Data Load  - Failed",
    html_content="UK Sales Data Load Failed. Please check the logs for more details.",
    dag=dag,
    trigger_rule="all_failed",
)

# Task for LatestOnlyOperator branch
latest_only = LatestOnlyOperator(
    task_id="latest_only",
    dag=dag)

# Connect tasks
task_a >> task_b >> send_email_failed
task_b >> latest_only >> send_email_completed