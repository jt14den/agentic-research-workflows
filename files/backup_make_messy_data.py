import pandas as pd
import numpy as np
import os

# Create a data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Site A
site_a = pd.DataFrame({
    'ParticipantID': range(101, 151),
    'Date': pd.date_range(start='2023-01-01', periods=50),
    'Score': np.random.randint(50, 100, size=50)
})
site_a.loc[5, 'Score'] = np.nan
site_a.to_csv('site_A.csv', index=False)

# Site B
site_b = pd.DataFrame({
    'id': range(201, 251),
    'date_time': pd.date_range(start='2023-02-01', periods=50),
    'Score': np.random.randint(40, 95, size=50)
})
site_b.loc[10, 'Score'] = np.nan
# Change some date formats
site_b['date_time'] = site_b['date_time'].dt.strftime('%b %d, %Y')
site_b.to_csv('site_B.csv', index=False)

# Site C
site_c = pd.DataFrame({
    'ID': range(301, 351),
    'DATE': pd.date_range(start='2023-03-01', periods=50),
    'Value': np.random.randint(60, 100, size=50)
})
site_c.loc[15, 'Value'] = np.nan
# Change some date formats
site_c['DATE'] = site_c['DATE'].dt.strftime('%Y/%m/%d')
site_c.to_csv('site_C.csv', index=False)

print("Generated site_A.csv, site_B.csv, site_C.csv")
