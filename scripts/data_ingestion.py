import pandas as pd
from pathlib import Path

# Define raw data folder
raw_data_path = Path("data/raw")

# Get all CSV files
csv_files = list(raw_data_path.glob("*.csv"))

print("=" * 60)
print("BLUESTOCK MUTUAL FUND ANALYTICS")
print("DATA INGESTION REPORT")
print("=" * 60)

# Loop through every CSV file
for file in csv_files:

    print("\n" + "=" * 60)
    print(f"Dataset: {file.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file)

        print(f"Rows, Columns: {df.shape}")
        print("\nColumn Names:")
        print(list(df.columns))

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}")
        print(e)

print("\n")
print("=" * 60)
print("DATA INGESTION COMPLETED")
print("=" * 60)