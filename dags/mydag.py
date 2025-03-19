from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'job_scraping_dag',
    default_args=default_args,
    description='A web scraping DAG to scrape job listings from wuzzuf.net and transform with PySpark, then load to PostgreSQL',
    schedule_interval='@daily',  
    start_date=datetime(2025, 3, 19),
    catchup=False,  
) as dag:

    # Scraping job task using BashOperator
    scrape_job_task = BashOperator(
        task_id='scrape_jobs',
        bash_command='python3 /usr/local/airflow/include/scripts/scraper.py',  
        dag=dag,
    )

    # Spark task
    spark_task = SparkSubmitOperator(
        task_id='spark_task',
        conn_id='my_spark',  
        application='/usr/local/airflow/include/scripts/spark_processor.py',
        verbose=True,  # Enable verbose logging
        conf={'spark.master': 'spark://spark-master:7077'},  # Spark master URL
        dag=dag
    )

    load_data_task = BashOperator(
        task_id='load_data_to_postgres',
        bash_command='python3 /usr/local/airflow/include/scripts/db_loader.py',  # Use Bash to run the script
        dag=dag,
    )

    # Set task dependencies
    scrape_job_task >> spark_task >> load_data_task
