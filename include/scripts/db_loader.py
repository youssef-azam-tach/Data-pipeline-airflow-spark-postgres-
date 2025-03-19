from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

def load_data_to_postgres():
    db_config = {
        "dbname": "postgres",
        "user": "postgres",  #
        "password": "postgres",  
        "host": "postgres",  
        "port": 5432  
    }
    
    input_file = './include/data/job_listings_transformed.csv'  
    df = pd.read_csv(input_file, header=0)  

    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS jobs (
        job_name VARCHAR(255),
        company_name VARCHAR(255),
        location VARCHAR(255),
        exp_level VARCHAR(255),
        exp_years VARCHAR(255),
        skills TEXT,
        avg_exp VARCHAR(255)
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    
    insert_query = """
    INSERT INTO jobs (
        job_name, company_name, location, exp_level, exp_years, skills, avg_exp
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, (
            row['job_name'], row['company_name'], row['location'],
            row['exp_level'], row['exp_years'], row['skills'], row['avg_exp']
        ))

    connection.commit()
    print("Data loaded into PostgreSQL successfully.")

    cursor.close()
    connection.close()