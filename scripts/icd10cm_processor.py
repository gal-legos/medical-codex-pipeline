# icd10cm_processor.py
import pandas as pd

 

# Read the file with no header and assign column names
df = pd.read_csv('input/icd10cm_order_2025.txt', sep='\t', header=None, names=['code', 'description'])

# Add the last_updated column
df['last_updated'] = '2025-09-01'

# Save to CSV without the index
df.to_csv('output/icd10cm_2025.csv', index=False)

print('icd10cm_2025.csv created with columns: code, description, last_updated')


output_path = 'output/icd10cm_small.csv'

 

