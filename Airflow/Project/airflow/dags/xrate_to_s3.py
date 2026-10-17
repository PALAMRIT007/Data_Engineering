from datetime import datetime
import subprocess

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator  # CHANGED: airflow.operators.python -> providers.standard
from airflow.sdk import Variable  # CHANGED: airflow.models -> airflow.sdk
# CHANGED: days_ago aur LocalFilesystemToS3Operator ke imports hata diye

dag = DAG(
    'xrate_to_s3',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 23 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False
)

def fetch_xrate_fn(ti):
    xrate_filename = f'xrate_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json'
    curl_command = ["curl", Variable.get('web_api_key'), "-o", f'/tmp/{xrate_filename}']
    subprocess.run(curl_command, check=True)  # CHANGED: check=True, taaki curl fail ho to task bhi fail ho
    ti.xcom_push(key='xrate_file', value=xrate_filename)

fetch_xrate = PythonOperator(
    task_id='fetch_xrate',
    python_callable=fetch_xrate_fn,
    # CHANGED: provide_context hata diya (Airflow 3 mein zarurat nahi)
    dag=dag
)


# Use this when you have the aws s3 cred.
# upload_to_s3 = LocalFilesystemToS3Operator(
#     task_id='upload_to_s3',
#     filename="/tmp/{{ ti.xcom_pull(task_ids='fetch_xrate', key='xrate_file') }}",
#     dest_bucket='sleek-data',
#     dest_key=f'oms/{{{{ ti.xcom_pull(task_ids="fetch_xrate", key="xrate_file") }}}}',
#     aws_conn_id='aws_conn',
#     dag=dag
# )



# CHANGED: LocalFilesystemToS3Operator ki jagah custom function (S3 na hone par workaround)
def upload_to_s3_fn(ti):
    xrate_filename = ti.xcom_pull(task_ids='fetch_xrate', key='xrate_file')
    # Yahan real upload nahi ho raha, sirf notification hai
    print(f"File {xrate_filename} uploaded to S3 successfully (simulated, S3 not configured)")

upload_to_s3 = PythonOperator(
    task_id='upload_to_s3',
    python_callable=upload_to_s3_fn,
    dag=dag
)

# Define Dependencies
fetch_xrate >> upload_to_s3