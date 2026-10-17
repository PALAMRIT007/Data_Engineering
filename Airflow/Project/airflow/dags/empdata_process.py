from datetime import datetime  # CHANGED: days_ago hata diya

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.snowflake.transfers.copy_into_snowflake import CopyFromExternalStageToSnowflakeOperator

dag = DAG(
    's3_to_snowflake_dag',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 23 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False
)

# Wait for the file in S3
wait_for_file = S3KeySensor(
    task_id='wait_for_s3_file',
    bucket_name='sleekdata',
    bucket_key='oms/employee_details.csv',
    aws_conn_id='aws_conn',
    poke_interval=10,
    timeout=60 * 60 * 5,
    soft_fail=True,
    deferrable=True,
    dag=dag
)

# Load the file from S3 to Snowflake
load_table = CopyFromExternalStageToSnowflakeOperator(
    task_id="load_s3_file_to_table",
    snowflake_conn_id="snowflake_conn",
    files=["employee_details.csv"],
    table="SLEEKMART_OMS.L1_LANDING.employee_details",
    stage='my_s3_stage',
    file_format="(type = 'CSV',field_delimiter = ',', skip_header = 1)",
    dag=dag
)

# Set the dependencies
wait_for_file >> load_table