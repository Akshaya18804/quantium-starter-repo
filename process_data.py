import pandas as pd
from pathlib import Path

data_folder = Path("data")
csv_files = data_folder.glob("*.csv")

all_data = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keep only pink morsel rows (case-sensitive match)
    df = df[df["product"] == "pink morsel"]

    # Remove $ sign and convert price to float
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

    # Calculate sales
    df["Sales"] = df["price"] * df["quantity"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]

    all_data.append(df)

# Combine all three CSVs
final_df = pd.concat(all_data, ignore_index=True)

# Rename columns
final_df.columns = ["Sales", "Date", "Region"]

# Save output
final_df.to_csv("pink_morsels_sales.csv", index=False)

print("✅ pink_morsels_sales.csv generated successfully")
