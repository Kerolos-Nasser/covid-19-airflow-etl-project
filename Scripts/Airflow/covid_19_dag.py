from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.S3_hook import S3Hook
import pandas as pd


def run_filter_data():
    # Read the CSV file
    df = pd.read_csv('/root/airflow/covid_dag/covid-19.csv')
    df = df.drop(df.index[216:])
    df = df.fillna(0)
    df.to_csv('/root/airflow/covid_dag/covid-19-cleaned.csv', index=False)



def upload_to_s3(filename: str, key: str, bucket_name: str) -> None:
    hook = S3Hook('s3_conn')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)



with DAG(
    dag_id='s3_dag',
    schedule_interval='@daily',
    start_date=datetime(2023, 5, 1),
    catchup=False
) as dag:



    # Filter the csv
    filter_csv = PythonOperator(
    task_id='filter_csv',
    python_callable=run_filter_data,
    dag=dag, 
)
    
    # Upload the file
    task_upload_to_s3 = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={
            'filename': '/root/airflow/covid_dag/covid-19-cleaned.csv',
            'key': 'covid-19-cleaned.csv',
            'bucket_name': 'covid-19-airflow'
        }
    )




filter_csv >> task_upload_to_s3
