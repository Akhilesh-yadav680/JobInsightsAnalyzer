import requests
from bs4 import BeautifulSoup
import pandas as pd

# Job listings URL
url = 'https://realpython.github.io/fake-jobs/'

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job cards
jobs = soup.find_all('div', class_='card-content')

# Store data
job_list = []

for job in jobs:
    title = job.h2.text.strip()
    company = job.h3.text.strip()
    location = job.find('p', class_='location').text.strip()
    link = job.a['href']  # Job link
    
    job_list.append({'Title': title, 'Company': company, 'Location': location, 'URL': link})

# Save to CSV
df = pd.DataFrame(job_list)
df.to_csv('job_listings.csv', index=False)
print(f"Scraped {len(job_list)} jobs and saved to 'job_listings.csv'")
