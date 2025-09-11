
import pandas as pd

# Read the fixed-width file (adjust colspecs as needed)
colspecs = [(3, 13), (13, 93)]  
hcps_data = pd.read_fwf('input/HCPC2025_OCT_ANWEB_v3.txt',
                         colspecs=colspecs, header=None,
                           names=['code', 'description'])

# Remove leading/trailing spaces
hcps_data['code'] = hcps_data['code'].str.strip()
hcps_data['description'] = hcps_data['description'].str.strip()

# Removing duplicates
hcps_data = hcps_data.drop_duplicates(subset=['code', 'description'])

# Add last_updated column
hcps_data['last_updated'] = '2025-09-01'

# Save to CSV
hcps_data.to_csv('output/hcps_cleaned.csv', index=False)

print('Saved cleaned HCPCS data to output/hcps_cleaned.csv')

