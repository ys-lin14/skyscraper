import pendulum
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from modules.scrape_sky_reviews import scrape_review_data

local_tz = pendulum.timezone('America/Vancouver')

default_args = dict(
    owner='Derek Yung-Sheng Lin',
    start_date=datetime(2021, 5, 12, tzinfo=local_tz),
    email=['ys.lin113@gmail.com'],
    email_on_failure=True,
    retries=0
)

dag = DAG(
    'Sky_DAG', 
    description="Scrape yesterday's Google Play reviews for Sky: COTL every day at 12:12 a.m.",
    schedule_interval='12 0 * * *',
    default_args=default_args,
    catchup=False
)

scrape_sky_reviews_python_operator = PythonOperator(
    task_id='scrape_sky_task',
    python_callable=scrape_review_data,
    op_kwargs={'execution_date': '{{ next_ds }}'},
    dag=dag
)

scrape_sky_reviews_python_operator
