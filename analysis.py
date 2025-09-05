import pandas as pd

df = pd.read_csv('job_listings_cleaned.csv')

# Top 10 companies by number of job listings
top_companies = df['Company'].value_counts().head(10)
print("Top 10 Companies:\n", top_companies)

# Top 10 locations
top_locations = df['Location'].value_counts().head(10)
print("Top 10 Locations:\n", top_locations)

# Most common job titles
top_titles = df['Title'].value_counts().head(10)
print("Top 10 Job Titles:\n", top_titles)
