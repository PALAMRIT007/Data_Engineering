from datetime import datetime  # CHANGED: days_ago hata diya

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator  # CHANGED: python_operator -> providers.standard

# CHANGED: S3Hook import comment kiya. Amazon provider abhi image mein nahi hai,
# to ye import DAG ko hi fail kar deta.
# AWS ready hone par uncomment karo (naya path: airflow.providers.amazon.aws.hooks.s3)

# from airflow.providers.amazon.aws.hooks.s3 import S3Hook

# ORIGINAL function (AWS ready hone par uncomment karo, aur neeche wala stub hata do)
# def custom_transformation(bucketname, sourcekey, destinationkey):
#     s3_hook = S3Hook(aws_conn_id='aws_conn')
#     # Read S3 File
#     content = s3_hook.read_key(bucket_name=bucketname, key=sourcekey)
#
#     # Apply Custom Transformations
#     transformed_content = content.upper()
#
#     # Load S3 File
#     s3_hook.load_string(transformed_content, bucket_name=bucketname, key=destinationkey)


# STUB function (temporary, S3 na hone par DAG fail na ho)
def custom_transformation(bucketname, sourcekey, destinationkey):
    print(
        f"Simulated: s3://{bucketname}/{sourcekey} -> upper-case -> "
        f"s3://{bucketname}/{destinationkey} (S3 not configured, no real transformation done)"
    )

    return "ho gyaaa"


# Define DAG
dag = DAG(
    'cust_s3_trans',
    start_date=datetime(2026, 10, 15),  # CHANGED: default_args se bahar
    schedule='0 23 * * *',  # CHANGED: schedule_interval -> schedule
    catchup=False
)

# Define your tasks
transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=custom_transformation,
    op_args=['sleek-data', 'oms/customer.csv', 'oms/customer_transformed.csv'],  #will change this to my bucket names
    dag=dag,
)

# Define Dependencies
transform_task