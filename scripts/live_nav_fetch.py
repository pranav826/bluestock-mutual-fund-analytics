import requests
import pandas as pd

scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

print("Scheme Name:")
print(data["meta"]["scheme_name"])

print("\nFund House:")
print(data["meta"]["fund_house"])

print("\nLatest NAV:")
print(data["data"][0])

# Save NAV history
nav_df = pd.DataFrame(data["data"])

nav_df.to_csv(
    "data/raw/live_nav_125497.csv",
    index=False
)

print("\nNAV data saved successfully.")