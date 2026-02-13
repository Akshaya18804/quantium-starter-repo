import pandas as pd
from pathlib import Path

# Path to data folder
data_folder = Path("data")

# Read all CSV files in the data folder
csv_files = data_folder.glob("*.csv")

dataframes = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["Sales", "date", "region"]]

    dataframes.append(df)

# Combine all data into one DataFrame
final_df = pd.concat(dataframes, ignore_index=True)

# Rename columns to match required output format
final_df.columns = ["Sales", "Date", "Region"]

# Save output file
final_df.to_csv("pink_morsels_sales.csv", index=False)

print("✅ Output file created: pink_morsels_sales.csv")
