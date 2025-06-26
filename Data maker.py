import pandas as pd
import numpy as np
import random
# Settings
num_rows = 1000 # Factory workers
num_columns = 12  # Data columns
# Base columns (will be reused in patterns)
worker_ids = [f"W{1000 + i}" for i in range(num_rows)]
ages = np.random.randint(20, 60, size=num_rows)
experience_years = [random.randint(0, age - 20) for age in ages]
departments = np.random.choice(['Assembly', 'Maintenance', 'Packaging', 'QC', 'Logistics'], size=num_rows)
# Start the dataframe
df = pd.DataFrame({
    'WorkerID': worker_ids,
    'Age': ages,
    'Experience': experience_years,
    'Department': departments
})
# Generate 9996 additional columns with related sensor/factory data
for i in range(1, num_columns - 4):  # -3 because we already added 4 columns above
    col_name = f"Sensor_{i}"
    # Example logic: related to experience and age, with noise
    df[col_name] = df['Experience'] * np.random.uniform(0.5, 1.5) + np.random.normal(0, 5, size=num_rows)
    # Insert NaNs randomly for data cleaning practice
    mask = np.random.rand(num_rows) < 0.05  # ~5% missing
    df.loc[mask, col_name] = np.nan
# Save to CSV
df.to_csv("factory_worker_data.csv", index=False)
print("CSV with 10,000+ columns and realistic values generated successfully.")
