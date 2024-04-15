# Library Imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt
from airflow.utils.dates import days_ago


# DAG Arguments
default_args = {
  'owner': 'airflow',
  'start_date': days_ago(0),
  'email': ['s.stuti990@gmail.com'],
}

# DAG Definition
dag=DAG(
  'process_web_log',
  description='SoftCart access log ETL pipeline',
  default_args=default_args,
  schedule_interval=dt.timedelta(days=1),
)

# Task Definitions

# extract data
extract_data = BashOperator(
  task_id='extract_data',
  bash_command='cut -f1 -d" " $AIRFLOW_HOME/dags/capstone/accesslog.txt > $AIRFLOW_HOME/dags/capstone/extracted_data.txt',
  dag=dag,
)

# transform data
transform_data = BashOperator(
  task_id='transform_data',
  bash_command='grep -vw "198.46.149.143" $AIRFLOW_HOME/dags/capstone/extracted_data.txt > $AIRFLOW_HOME/dags/capstone/transformed_data.txt',
  dag=dag,
)

#load data
load_data = BashOperator(
  task_id='load_data',
  bash_command='tar -zcvf $AIRFLOW_HOME/dags/capstone/weblog.tar $AIRFLOW_HOME/dags/capstone/transformed_data.txt',
  dag=dag,
)

# Task Pipeline
extract_data >> transform_data >> load_data