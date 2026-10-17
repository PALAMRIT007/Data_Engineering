from datetime import datetime  # CHANGED: days_ago hata diya

from airflow import DAG
from airflow.sdk import task  # CHANGED: airflow.decorators -> airflow.sdk
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator  # CHANGED: SnowflakeOperator ki jagah

@task
def extract():
    # Extract logic here
    return "Raw order data"

@task
def transform(raw_data):
    # Transform logic here
    return f"Processed: {raw_data}"

@task
def validate(processed_data):
    # Validate logic here
    return f"Validated: {processed_data}"

@task
def load(validated_data):
    # Load logic here
    print(f"Data loaded successfully: {validated_data}")

dag = DAG(
    'hybrid_dag',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 21 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False
)

with dag:
    load_task = load(validate(transform(extract())))

    # snowflake_task = SQLExecuteQueryOperator(  # CHANGED
    #     task_id='Snowflake_task',
    #     sql='select 1',
    #     conn_id='snowflake_conn',  # CHANGED: snowflake_conn_id -> conn_id
    # )

    # load_task >> snowflake_task


# commented part is to demonstrate we can make use of traditional 
# operators and taskflow apis in single code in hybrid manner.