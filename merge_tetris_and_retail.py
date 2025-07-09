import pandas as pd
import random

# Load cleaned Tetris data
tetris_df = pd.read_csv("tetris_blocks.csv")

# Load and inspect Retail data
retail_df = pd.read_csv("sales_data.csv", encoding='latin1', on_bad_lines='warn', engine='python')
print("COLUMNS:", retail_df.columns.tolist())  # <-- See actual column names

# Normalize and rename columns
# 🧹 Clean BOM and normalize column names
retail_df.columns = retail_df.columns.str.replace('ï»¿', '').str.strip().str.upper()

retail_df.rename(columns={
    'ITEM TYPE': 'ITEM_TYPE',
    'RETAIL SALES': 'RETAIL_SALES',
    'WAREHOUSE SALES': 'WAREHOUSE_SALES'
}, inplace=True)

# Add synthetic Tetris-style columns
shape_map = {
    "WINE": "T",
    "BEER": "L",
    "SPIRITS": "Z",
    "READY TO DRINK": "O"
}
retail_df["BlockShape"] = retail_df["ITEM_TYPE"].map(shape_map).fillna("I")
retail_df["Color"] = retail_df["BlockShape"].map({
    "T": "Red", "L": "Blue", "Z": "Green", "O": "Yellow", "I": "Purple"
})
retail_df["Region"] = [random.choice(["North", "South", "East", "West"]) for _ in range(len(retail_df))]
retail_df["Revenue"] = retail_df["RETAIL_SALES"].fillna(0) + retail_df["WAREHOUSE_SALES"].fillna(0)
retail_df["QuantitySold"] = retail_df["Revenue"] // random.randint(80, 150)
retail_df["Date"] = pd.to_datetime({
    'year': retail_df['YEAR'],
    'month': retail_df['MONTH'],
    'day': 1
}).dt.strftime('%Y-%m-%d')

# Select compatible columns only
retail_df_final = retail_df[[
    "Date", "BlockShape", "Color", "Region", "QuantitySold", "Revenue"
]]

# Combine both datasets
merged_df = pd.concat([tetris_df, retail_df_final], ignore_index=True)

# Save final unified file
merged_df.to_csv("dashboard_data.csv", index=False)
print("✅ Merged dataset saved as dashboard_data.csv")
