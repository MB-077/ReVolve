import pandas as pd

# Load the dataset
df = pd.read_csv('tagging_data.csv')

# Identify rows with inconsistent lengths
df['Token_length'] = df['Token_list'].apply(lambda x: len(x.split(',')))
df['Label_length'] = df['Label_list'].apply(lambda x: len(x.split(',')))

# Find inconsistent rows
inconsistent_rows = df[df['Token_length'] != df['Label_length']]

# Log inconsistent rows
print("Inconsistent rows:")
print(inconsistent_rows)

# Filter out inconsistent rows
consistent_df = df[df['Token_length'] == df['Label_length']]

# Drop the temporary length columns
consistent_df = consistent_df.drop(columns=['Token_length', 'Label_length'])

# Save the cleaned dataset
consistent_df.to_csv('clean_tagged_data.csv', index=False)

# Print the number of rows removed
print(f"Removed {len(inconsistent_rows)} inconsistent rows")
