from datetime import datetime  # CHANGED: days_ago hata diya, datetime use hoga
import logging

from airflow import DAG
from airflow.providers.github.operators.github import GithubOperator
from airflow.providers.standard.operators.empty import EmptyOperator  # CHANGED: DummyOperator -> EmptyOperator

# Define the DAG
# CHANGED: start_date direct DAG mein, schedule_interval -> schedule
dag = DAG(
    'git_repo_dag',
    start_date=datetime(2026, 10, 15),
    schedule='0 21 * * *',
    catchup=False
)

# Start Empty Operator
start = EmptyOperator(task_id='start', dag=dag)  # CHANGED

# List GitRepository Tags
list_repo_tags = GithubOperator(
    task_id="list_repo_tags",
    # github_conn_id="github_default",  # connection ka naam (Admin -> Connections mein banana hai)
    github_method="get_repo",
    github_method_args={"full_name_or_id": "PALAMRIT007/Data_Engineering"},
    result_processor=lambda repo: logging.info(list(repo.get_tags())),
    dag=dag,
)

# End Empty Operator
end = EmptyOperator(task_id='end', dag=dag)  # CHANGED

# Define task dependencies
start >> list_repo_tags >> end