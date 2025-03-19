from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import re

spark = SparkSession.builder \
    .appName("Job Listings Transformation") \
    .getOrCreate()

input_path = "/usr/local/airflow/include/job_listings.csv"
output_path = "/usr/local/airflow/include/data/job_listings_transformed.csv"

df = spark.read.csv(input_path, header=True, inferSchema=True)

df = df.toDF(*[c.lower().replace(" ", "_") for c in df.columns])

def extract_experience(exp_years):
    try:
        numbers = re.findall(r'\d+', exp_years)
        
        if len(numbers) == 1:
            return int(numbers[0])
        elif len(numbers) > 1:
            return sum([int(num) for num in numbers]) // len(numbers)
        
    except Exception:
        return exp_years

spark.udf.register("extract_experience", extract_experience)

df = df.withColumn("avg_exp", F.expr("extract_experience(exp_years)"))


df.toPandas().to_csv(output_path, index=False)

spark.stop()
