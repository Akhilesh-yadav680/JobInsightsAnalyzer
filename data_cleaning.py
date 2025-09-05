import pandas as pd

# Load scraped data
df = pd.read_csv('job_listings.csv')

# Remove duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Optional: reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned data
df.to_csv('job_listings_cleaned.csv', index=False)
print(f"Data cleaned and saved as 'job_listings_cleaned.csv'. Total rows: {len(df)}")
