import pandas as pd
import glob

# Find all CSV files in the data directory
csv_files = glob.glob("data/*.csv")

combined_df = []

for file in csv_files:
    df = pd.read_csv(file)

    # Standardize column names to lowercase to handle format differences
    df.columns = df.columns.str.lower()

    # Filter for only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Clean price column (remove '$' sign if present) and convert types
    df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)
    df["quantity"] = df["quantity"].astype(int)

    # Calculate total sales
    df["sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    combined_df.append(df)

# Combine all data and export to a single CSV file
final_df = pd.concat(combined_df, ignore_index=True)
final_df.to_csv("formatted_data.csv", index=False)

print("Data processing complete. 'formatted_data.csv' created successfully.")