# **Data Pipeline with Airflow, Spark,PostgreSQL and Power BI**

## **Project Overview**

This project is a comprehensive data pipeline designed to automate the process of scraping job listings from Wuzzuf.net, processing the data using Apache Spark, and storing the transformed data into a PostgreSQL database. The workflow is orchestrated using Apache Airflow for automation, and Docker is used for containerization, ensuring consistency across environments.

- **Full Pipeline Overview**:  
  ![Full Pipeline Overview](https://raw.githubusercontent.com/youssef-azam-tach/Data-pipeline-airflow-spark-postgres-/main/images/Full-pipline.png)
---

## **Key Components**

1. **Web Scraping**:
   - A Python script (`scraper.py`) scrapes job listings from Wuzzuf.net.
   - Extracts job details such as job title, company name, location, experience level, and required skills.
   - Saves the data as a CSV file (`job_listings.csv`).

2. **Data Transformation with Apache Spark**:
   - A Spark job (`spark_processor.py`) processes the scraped data.
   - Cleans and transforms the data, normalizing column names, extracting average experience years, and saves the transformed data as a new CSV file (`job_listings_transformed.csv`).

3. **Data Loading into PostgreSQL**:
   - A Python script (`db_loader.py`) loads the transformed data into a PostgreSQL database.
   - Creates a `jobs` table if it doesn't exist and inserts the data into the table.

4. **Orchestration with Apache Airflow**:
   - The Airflow DAG (`mydag.py`) orchestrates the entire workflow.
   - The DAG consists of three tasks:
     - **Scraping Task**: Runs the web scraping script.
     - **Spark Task**: Submits the Spark job for data transformation.
     - **Loading Task**: Loads the transformed data into PostgreSQL.

5. **Docker Compose Configuration**:
   - Docker Compose is used to manage services such as PostgreSQL, Spark, and Airflow.
   - The `docker-compose.override.yml` file defines additional services like Spark Master, Spark Worker, and pgAdmin for PostgreSQL management.

---

## **Project Structure**

```
project/
├── .astro/
│ ├── config.yaml
│ ├── dag_integrity_exceptions.txt
│ ├── test_dag_integrity_default.py
├── dags/
│ ├── mydag.py
│ ├── .airflowignore
├── include/
│ ├── data/
│ │ └── job_listings_transformed.csv
│ ├── scripts/
│ │ ├── db_loader.py
│ │ ├── scraper.py
│ │ └── spark_processor.py
├── images/
│ ├── ALL-Docker-Containers.jpg
│ ├── Airflow-UI.jpg
│ ├── Data-Pipline airflow.jpg
│ ├── Full-pipline.png
│ ├── Spark-UI.jpg
│ └── postgrs-page-admin.jpg
├── Dockerfile
├── docker-compose.override.yml
├── .dockerignore
├── .gitignore
├── requirements.txt
├── packages.txt
└── tests/
    └── dags/test_dag_example.py
```

---

## **Images**

The following images are included in the project, showcasing various components of the pipeline:

- **Docker Containers Overview**:  
  ![Docker Containers Overview](https://raw.githubusercontent.com/youssef-azam-tach/Data-pipeline-airflow-spark-postgres-/main/images/ALL-Docker-Containers.jpg)

- **Airflow UI**:  
  ![Airflow UI](https://raw.githubusercontent.com/youssef-azam-tach/Data-pipeline-airflow-spark-postgres-/main/images/Airflow-UI.jpg)

- **Data Pipeline in Airflow**:  
  ![Data Pipeline in Airflow](https://raw.githubusercontent.com/youssef-azam-tach/Data-pipeline-airflow-spark-postgres-/main/images/Data-Pipline%20airflow.jpg)

- **Spark UI**:  
  ![Spark UI](https://raw.githubusercontent.com/youssef-azam-tach/Data-pipeline-airflow-spark-postgres-/main/images/Spark-UI.jpg)

- **PostgreSQL Admin UI**:  
  ![PostgreSQL Admin UI](https://raw.githubusercontent.com/youssef-azam-tach/Data-pipeline-airflow-spark-postgres-/main/images/postgrs-page-admin.jpg)

---

## **How to Run the Project**

1. **Prerequisites**:
   - Docker and Docker Compose installed.
   - Git installed.

2. **Steps**:
   - Clone the repository:
     ```bash
     git clone <repository-url>
     cd <project-folder>
     ```
   - Start the Airflow environment:
     ```bash
     astro dev start
     ```
   - Access the Airflow UI at `http://localhost:8080`.
   - Trigger the DAG (`job_scraping_dag`) manually or wait for the scheduled run.

3. **Access Services**:
   - **Airflow UI**: `http://localhost:8080`
   - **pgAdmin**: `http://localhost:5050`
   - **Spark Master UI**: `http://localhost:8081`

---

## **Challenges and Solutions**

### 1. **Problem: Airflow DAG Failing to Trigger Jobs**
   - **Issue**: The Airflow DAG failed to trigger jobs in a timely manner due to incorrect task dependencies and a misconfigured DAG schedule.
   - **Cause**: The `depends_on_past` parameter was set to `True`, causing tasks to fail if previous runs didn’t complete successfully.
   - **Solution**: Removed `depends_on_past` and ensured the DAG schedule was correctly configured for task execution.  

### 2. **Problem: Spark Job Timing Out**
   - **Issue**: Spark jobs were timing out during the execution of the data transformation process.
   - **Cause**: The default executor memory allocated in Docker for Spark was insufficient for the data being processed.
   - **Solution**: Increased the memory allocation for the Spark containers in the `docker-compose.override.yml` file.

### 3. **Problem: PostgreSQL Connection Failure**
   - **Issue**: The `db_loader.py` script failed to connect to PostgreSQL.
   - **Cause**: The PostgreSQL service wasn't fully initialized before the connection attempt.
   - **Solution**: Added a retry mechanism with a delay in the script to ensure that the connection is attempted only after PostgreSQL is ready.

---

## **Conclusion**

This project demonstrates how to build a scalable and automated data pipeline using Apache Airflow, Apache Spark, and PostgreSQL. By incorporating Docker, the solution is containerized and can be easily deployed across different environments. The automation of job scraping, transformation, and loading provides a streamlined and efficient process for handling large amounts of job data.

The challenges encountered during development were addressed using best practices for task dependencies, resource management, and robust error handling.

---
