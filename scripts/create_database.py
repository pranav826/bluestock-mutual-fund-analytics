import sqlite3
import pandas as pd

from pathlib import Path
from sqlalchemy import create_engine

print("=" * 60)
print("CREATING SQLITE DATABASE")
print("=" * 60)

# Project folders
db_path = Path("db/bluestock_mf.db")
schema_path = Path("sql/schema.sql")

# Connect to database
conn = sqlite3.connect(db_path)

print("Database connected successfully.")

# Read schema.sql

with open(schema_path, "r") as file:
    schema = file.read()

print("Schema loaded successfully.")

# Execute schema

conn.executescript(schema)

print("Tables created successfully.")

conn.commit()
conn.close()

print("\nCreating SQLAlchemy Engine...")

engine = create_engine(
    "sqlite:///db/bluestock_mf.db"
)

print("Engine created successfully.")

print("Database saved successfully.")
print("=" * 60)

print("\nLoading Fund Master...")

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)

print("dim_fund loaded.")

print("\nLoading NAV History...")

nav = pd.read_csv(
    "data/processed/02_nav_history.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)

print("fact_nav loaded.")

print("\nLoading Investor Transactions...")

transactions = pd.read_csv(
    "data/processed/08_investor_transactions.csv"
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

print("fact_transactions loaded.")

print("\nLoading Scheme Performance...")

performance = pd.read_csv(
    "data/processed/07_scheme_performance.csv"
)

# Keep only fact table columns
performance = performance[
    [
        "amfi_code",
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
        "morningstar_rating",
        "risk_grade",
    ]
]

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

print("fact_performance loaded.")

print("\nLoading AUM Data...")

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="append",
    index=False
)

print("fact_aum loaded.")

print("\n" + "=" * 60)
print("VERIFYING TABLE ROW COUNTS")
print("=" * 60)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

conn = sqlite3.connect("db/bluestock_mf.db")
cursor = conn.cursor()

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} rows")

conn.close()