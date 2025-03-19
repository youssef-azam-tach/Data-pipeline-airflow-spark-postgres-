---

# Job Scraping and Data Pipeline with Airflow, Spark, and PostgreSQL

This project implements a scalable data pipeline that scrapes job listings from a job portal (Wuzzuf.net), processes the data using Apache Spark, and loads the transformed data into a PostgreSQL database. The entire workflow is orchestrated using **Apache Airflow**, ensuring automation, scalability, and reliability.

---

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Key Components](#key-components)
3. [Project Structure](#project-structure)
4. [How to Run the Project](#how-to-run-the-project)
5. [Screenshots](#screenshots)
6. [Key Features](#key-features)
7. [Conclusion](#conclusion)

---

## **Project Overview**

This project automates the process of scraping, transforming, and loading job listing data. It leverages a combination of modern technologies to ensure performance, scalability, and maintainability.

- **Apache Airflow** orchestrates the entire pipeline.
- **Apache Spark** is used for data transformation and processing.
- **PostgreSQL** stores the processed data for long-term storage and querying.
- **Docker Compose** is used for managing the services like Airflow, Spark, and PostgreSQL.

---

## **Key Components**

1. **Web Scraping**:
   - **Python Script**: Scrapes job listings from Wuzzuf.net.
   - **Data Extracted**: Job title, company name, location, experience level, required skills.
   - **Output**: Data saved to a CSV file (`job_listings.csv`).

2. **Data Transformation with Apache Spark**:
   - **Spark Job**: Processes the scraped data to clean, normalize, and transform the data.
   - **Output**: Transformed data saved to a new CSV file (`job_listings_transformed.csv`).

3. **Data Loading into PostgreSQL**:
   - **Python Script**: Loads the transformed data into a PostgreSQL database.
   - **Table Created**: `jobs` table, if it doesn't already exist.
   - **Data Insertion**: Inserts the transformed data into the `jobs` table.

4. **Orchestration with Apache Airflow**:
   - **DAG Definition**: Orchestrates the workflow, consisting of three tasks:
     - **Scraping Task**: Runs the web scraping script.
     - **Spark Task**: Runs the Spark job for data transformation.
     - **Loading Task**: Loads the transformed data into PostgreSQL.

5. **Docker Compose Configuration**:
   - Manages services like PostgreSQL, Spark, and Airflow in isolated containers.
   - Includes services for **Spark Master**, **Spark Worker**, and **pgAdmin**.

---

## **Project Structure**

```
project/
├── dags/
│ └── mydag.py
├── include/
│ ├── scripts/
│ │ ├── scraper.py
│ │ ├── spark_processor.py
│ │ └── db_loader.py
│ ├── data/
│ │ └── job_listings_transformed.csv
│ └── job_listings.csv
├── Dockerfile
├── docker-compose.override.yml
├── requirements.txt
├── airflow_settings.yaml
├── README.md
└── .gitignore
```

---

## **How to Run the Project**

### **Prerequisites**
- Docker and Docker Compose installed.
- Git installed.

### **Steps**
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

2. **Start the Airflow Environment**:
   ```bash
   astro dev start
   ```

3. **Access the Airflow UI**:
   Navigate to `http://localhost:8080` in your web browser.

4. **Trigger the DAG**:
   You can trigger the DAG (`job_scraping_dag`) manually or wait for the scheduled run.

5. **Access Services**:
   - **Airflow UI**: `http://localhost:8080`
   - **pgAdmin**: `http://localhost:5050`
   - **Spark Master UI**: `http://localhost:8081`

---

## **Screenshots**

### **Spark Master UI**
![Spark Master UI](images/photo_2025-03-18_22-42-15.jpg)

### **Airflow DAG Execution**
![Airflow DAG Execution](images/photo_2025-03-18_22-52-30.jpg)

### **Docker Containers Overview**
![Docker Containers Overview](images/photo_2025-03-18_22-58-43.jpg)

### **System Properties**
![System Properties](images/Screenshot_2025-03-18_163742.png)

---

## **Key Features**

- **Automation**: The workflow is fully automated with Apache Airflow, reducing manual intervention.
- **Scalability**: Apache Spark is used for processing large-scale data.
- **Data Storage**: PostgreSQL serves as a reliable and structured data storage solution.
- **Containerization**: Docker ensures that all services run in isolated environments, providing consistency across different setups.

---

## **Conclusion**

This project demonstrates a robust and scalable data pipeline solution for scraping, processing, and storing job listings. By integrating **Apache Airflow**, **Apache Spark**, and **PostgreSQL**, it provides a professional approach to handling data engineering tasks, ensuring high performance, scalability, and maintainability.

The project is well-documented, containerized, and ready for deployment. You can easily set it up on your local machine or deploy it on cloud infrastructure.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 
