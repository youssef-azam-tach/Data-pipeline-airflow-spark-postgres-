import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# Function to scrape jobs from wuzzuf.net
def scrape_jobs():
    df = pd.DataFrame(columns=["job_name", "company_name", "location", "exp_level", "exp_years", "skills"])
    
    # Loop through the pages
    for i in range(10):
        request = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=&start={i}")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="css-1gatmva e1v1l3u10")
        
        for job in jobs:
            job_name = job.find_all("h2", class_="css-m604qf")[0].text
            company_name = job.find_all("div", class_="css-d7j1kk")[0].text.split(" - ")[0]
            location = job.find_all("span", class_="css-5wys0k")[0].text.split(", ")[0]
            job_type = job.find_all("span", class_="css-1ve4b75 eoyjyou0")[0].text
            exp_level = job.find_all("div", class_="css-1lh32fc")[0].next_sibling.text.split(" · ")[0]
            exp_years = job.find_all("div", class_="css-1lh32fc")[0].next_sibling.text.split(" · ")[1]

            df.loc[len(df.index)] = [job_name, company_name, location, job_type, exp_level, exp_years]
        
        if i % 50 == 0:
            print(f"Page {i} done")
    
    # Save data to CSV
    df.to_csv("/usr/local/airflow/include/job_listings.csv", index=False)
    print("Scraping completed and data saved.")