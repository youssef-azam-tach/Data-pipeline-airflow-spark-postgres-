
---

# **Data Pipeline with Airflow, Spark, PostgreSQL, and Power BI**

## **Project Overview**

This project implements an end-to-end data pipeline to automate the process of scraping job listings from Wuzzuf.net, transforming the data using Apache Spark, and storing the transformed data into a PostgreSQL database. The pipeline is orchestrated with Apache Airflow, and Docker is utilized for containerization, ensuring consistent execution across different environments.

The workflow includes:
- **Web Scraping**: Collects job listings from Wuzzuf.net.
- **Data Transformation**: Uses Apache Spark for cleaning and transforming data.
- **Data Loading**: Loads the transformed data into PostgreSQL.
- **Orchestration**: Automates the pipeline using Apache Airflow.
- **Containerization**: Deploys the entire pipeline in Docker containers for consistency and scalability.

---

## **Full Pipeline Overview**

![Full Pipeline Overview](https://raw.githubusercontent.com/youssef-azam-tach/Data-pipeline-airflow-spark-postgres-/main/images/Full-pipline.png)

---

## **Key Components**

1. **Web Scraping**:
   - A Python script (`scraper.py`) scrapes job listings from Wuzzuf.net.
   - Extracts key job details, including:
     - Job title
     - Company name
     - Location
     - Experience level
     - Required skills
   - Saves the scraped data in a CSV file (`job_listings.csv`).

2. **Data Transformation with Apache Spark**:
   - A Spark job (`spark_processor.py`) processes the scraped data:
     - Cleans and normalizes column names
     - Extracts the average years of experience for each job listing
     - Saves the transformed data in a new CSV file (`job_listings_transformed.csv`).

3. **Data Loading into PostgreSQL**:
   - A Python script (`db_loader.py`) loads the transformed data into a PostgreSQL database.
   - Creates a `jobs` table if it doesn't already exist and inserts the cleaned data.

4. **Orchestration with Apache Airflow**:
   - The workflow is orchestrated using Apache Airflow through a Directed Acyclic Graph (DAG) (`mydag.py`).
   - The DAG consists of three tasks:
     - **Scraping Task**: Executes the web scraping script.
     - **Spark Task**: Submits the Spark job for data transformation.
     - **Loading Task**: Loads the transformed data into the PostgreSQL database.

5. **Docker Compose Configuration**:
   - Docker Compose is used to manage services for PostgreSQL, Spark, and Airflow.
   - The `docker-compose.override.yml` file configures services such as Spark Master, Spark Worker, and pgAdmin for PostgreSQL management.

---

## **Project Structure**

```
project/
├── .astro/
│   ├── config.yaml
│   ├── dag_integrity_exceptions.txt
│   ├── test_dag_integrity_default.py
├── dags/
│   ├── mydag.py
│   ├── .airflowignore
├── include/
│   ├── data/
│   │   └── job_listings_transformed.csv
│   ├── scripts/
│   │   ├── db_loader.py
│   │   ├── scraper.py
│   │   └── spark_processor.py
├── images/
│   ├── ALL-Docker-Containers.jpg
│   ├── Airflow-UI.jpg
│   ├── Data-Pipline airflow.jpg
│   ├── Full-pipline.png
│   ├── Spark-UI.jpg
│   └── postgrs-page-admin.jpg
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

## **Project Images**

The project includes several images to illustrate different components of the pipeline:

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

### **Prerequisites**
- Docker and Docker Compose installed.
- Git installed.

### **Steps**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```
2. Start the Airflow environment:
   ```bash
   astro dev start
   ```
3. Access the Airflow UI at `http://localhost:8080`.
4. Trigger the DAG (`job_scraping_dag`) manually or wait for the scheduled run.

### **Access Services**:
- **Airflow UI**: `http://localhost:8080`
- **pgAdmin**: `http://localhost:5050`
- **Spark Master UI**: `http://localhost:8081`

---

## **Challenges and Solutions**

### 1. **Problem: Airflow DAG Failing to Trigger Jobs**
   - **Issue**: The Airflow DAG failed to trigger jobs as expected due to task dependency misconfiguration.
   - **Cause**: Incorrect `depends_on_past` settings and a misconfigured DAG schedule.
   - **Solution**: Removed `depends_on_past` and ensured correct DAG scheduling.

### 2. **Problem: Spark Job Timing Out**
   - **Issue**: Spark jobs were timing out during the data transformation process.
   - **Cause**: Insufficient memory allocated for the Spark executor.
   - **Solution**: Increased memory allocation for the Spark containers in the `docker-compose.override.yml` file.

### 3. **Problem: PostgreSQL Connection Failure**
   - **Issue**: The `db_loader.py` script was unable to connect to PostgreSQL.
   - **Cause**: PostgreSQL service initialization was not completed before the connection attempt.
   - **Solution**: Implemented a retry mechanism with a delay in the script to ensure the connection is established once PostgreSQL is fully initialized.

---

## **Conclusion**

This project showcases a scalable and automated data pipeline utilizing Apache Airflow, Apache Spark, and PostgreSQL. The use of Docker containerization ensures consistent and repeatable deployments across different environments. The pipeline automates the process of scraping, transforming, and loading job data, offering a streamlined solution for data management.

Throughout the development process, key challenges were overcome by applying best practices in task orchestration, resource management, and error handling. This pipeline can be extended or adapted to suit other use cases involving large-scale data processing and automation.

---
