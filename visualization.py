import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('job_listings_cleaned.csv')

# Top 10 companies
top_companies = df['Company'].value_counts().head(10)
top_companies.plot(kind='bar', figsize=(10,5), color='skyblue')
plt.title('Top 10 Companies by Job Listings')
plt.ylabel('Number of Jobs')
plt.xlabel('Company')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 locations
top_locations = df['Location'].value_counts().head(10)
top_locations.plot(kind='bar', figsize=(10,5), color='orange')
plt.title('Top 10 Job Locations')
plt.ylabel('Number of Jobs')
plt.xlabel('Location')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
