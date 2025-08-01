from airflow import DAG
from datetime import datetime, timedelta
from plugins.custom_operators.upload_to_s3_operator import UploadToS3Operator as UploadToS3Operator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'abs_hasan',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    
}

with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1,
    tags=['weather', 'etl'],
    description='This DAG automates a data processing pipeline: it retrieves data, processes it, and updates external systems.',
    doc_md="""\
        # Data Processing Pipeline

        **Overview:**  
        This DAG automates a data processing workflow.

        **Process Steps:**  
        1. Retrieve data from a database.  
        2. Process the data.  
        3. Update results in external systems.

        **Schedule:** Once a week  
        **Owner:** Data Team
    """
) as dag:

    fetch_weather = PythonOperator(
        task_id='fetch_weather_data',
        python_callable=UploadToS3Operator,
    dag=dag
    )


