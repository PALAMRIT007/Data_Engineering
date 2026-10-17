# Imports
from datetime import datetime  # CHANGED: days_ago hata diya

from airflow import DAG
from airflow.providers.smtp.operators.smtp import EmailOperator  # CHANGED
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator  # CHANGED: SnowflakeOperator ki jagah


def notify_success():
    print('UK Sales table to Profit table Load Completed')


# Define the DAG
dag = DAG(
    'load_profit_uk',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 21 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False
)

# Define the Task
load_table = SQLExecuteQueryOperator(  # CHANGED
    task_id='load_table',
   sql='./sqls/profit_uk.sql',
    conn_id='snowflake_conn',  # CHANGED: snowflake_conn_id -> conn_id
    dag=dag
)

# send_email = EmailOperator(
#     task_id='send_email',
#     to="{{ var.value.get('support_email') }}",
#     subject='UK profit table load - Successful',
#     html_content='UK Sales table to Profit table Load Completed',
#     dag=dag,
# )

send_email = PythonOperator(
    task_id='send_email',
    python_callable=notify_success,
    dag=dag,
)



# Define the Dependencies
load_table >> send_email