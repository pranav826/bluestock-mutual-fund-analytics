import pandas as pd
from pathlib import Path

# Folder paths
raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

print("=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

print("\nCleaning NAV History...")

nav = pd.read_csv(raw_path / "02_nav_history.csv")

print("Original Shape:", nav.shape)

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"], format="%Y-%m-%d")

print("\nDate converted successfully.")
print(nav.dtypes)

# Sort by fund and date
nav = nav.sort_values(
    by=["amfi_code", "date"]
)

print("\nData sorted.")

before = len(nav)

nav = nav.drop_duplicates()

after = len(nav)

print(f"\nDuplicates removed: {before - after}")

invalid_nav = nav[nav["nav"] <= 0]

print("\nInvalid NAV Values:", len(invalid_nav))
print("\nMissing NAV values:")

print(nav["nav"].isnull().sum())

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

print("\nMissing NAV after fill:")

print(nav["nav"].isnull().sum())

nav.to_csv(
    processed_path / "02_nav_history.csv",
    index=False
)

print("\nCleaned NAV History saved successfully.")

# ======================================================
# CLEAN INVESTOR TRANSACTIONS
# ======================================================

print("\n" + "=" * 60)
print("Cleaning Investor Transactions...")
print("=" * 60)

transactions = pd.read_csv(raw_path / "08_investor_transactions.csv")

print("Original Shape:", transactions.shape)

# Convert transaction date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Remove duplicates
transactions = transactions.drop_duplicates()

print("Duplicates removed.")

# Validate amount
invalid_amounts = transactions[transactions["amount_inr"] <= 0]

print("Invalid Amounts:", len(invalid_amounts))

# Standardize transaction types
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

print("\nTransaction Types:")
print(transactions["transaction_type"].value_counts())

# KYC Status
print("\nKYC Status:")
print(transactions["kyc_status"].value_counts())

# Save cleaned file
transactions.to_csv(
    processed_path / "08_investor_transactions.csv",
    index=False
)

print("\nCleaned Investor Transactions saved successfully.")

# ======================================================
# CLEAN SCHEME PERFORMANCE
# ======================================================

print("\n" + "=" * 60)
print("Cleaning Scheme Performance...")
print("=" * 60)

scheme = pd.read_csv(raw_path / "07_scheme_performance.csv")

print("Original Shape:", scheme.shape)

# Remove duplicates
scheme = scheme.drop_duplicates()

print("Duplicates removed.")

# Convert numeric columns
numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
]

for col in numeric_columns:
    scheme[col] = pd.to_numeric(scheme[col], errors="coerce")

print("Numeric validation completed.")

# Check expense ratio
invalid_expense = scheme[
    (scheme["expense_ratio_pct"] < 0.1) |
    (scheme["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratios:", len(invalid_expense))

# Missing values
print("Missing Values:")
print(scheme.isnull().sum().sum())

# Save cleaned dataset
scheme.to_csv(
    processed_path / "07_scheme_performance.csv",
    index=False
)

print("\nCleaned Scheme Performance saved successfully.")