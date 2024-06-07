import pandas as pd

# Load the cleaned dataset
clean_df = pd.read_csv('clean_tagged_data.csv')

# Print the first few rows of the cleaned dataset
print("Sample of cleaned dataset:")
print(clean_df.head())

# Check the data types of the columns
print("\nData types:")
print(clean_df.dtypes)
