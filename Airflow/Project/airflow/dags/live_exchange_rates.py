# Import
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator  # CHANGED
from airflow.providers.smtp.operators.smtp import EmailOperator  # CHANGED

from datetime import datetime 
# Define the DAG
# dag = DAG(
#     'live_exchange_rates',
#     default_args={'start_date': days_ago(1)},
#     schedule_interval='0 23 * * *',
#     catchup=False
# )

dag = DAG(
    'live_exchange_rates',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 23 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False
)


# Define the Tasks
fetch_exchange_rates = BashOperator(
    task_id='fetch_exchange_rates',
    bash_command="curl '{{ var.value.get('web_api_key') }}' -o xrate.json",
    cwd='/tmp',
    dag=dag,
)

send_email_task = EmailOperator(
    task_id='send_email',
    to="{{ var.value.get('support_email') }}",
    subject='Live Exchange Rate Download - Successful.',
    html_content='Live Exchange Rate data has been successfully downloaded.',
    dag=dag,
)

# Define the Dependencies
fetch_exchange_rates >> send_email_task