
import pandas as pd

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Step 1: Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Step 2: Standardize 'Gender' values
df_cleaned['Gender'] = df_cleaned['Gender'].str.strip().str.capitalize()

# Step 3: Rename columns to lowercase and use underscores
df_cleaned.columns = (
    df_cleaned.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('(', '')
    .str.replace(')', '')
    .str.replace('-', '_')
)

# Step 4: Save cleaned dataset
df_cleaned.to_csv("Cleaned_Mall_Customers.csv", index=False)

# Optional: Show summary of changes
print("✅ Cleaning complete:")
print("- Duplicates removed:", df.duplicated().sum())
print("- Columns renamed:", df_cleaned.columns.tolist())
print("- Sample data:")
print(df_cleaned.head())
