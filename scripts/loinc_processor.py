import pandas as pd

loinc = pd.read_csv('input/loinc.csv')

## checking for potential columns 
loinc.info()

##finding columns 
loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]

loinc_small['last_updated'] = '2025-09-01'
loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code', 
    'LONG_COMMON_NAME': 'description', 
    'last_updated' : 'last_updated'
    })

file_output_path = 'output/loinc_small.csv'

loinc_small.to_csv(file_output_path, index=False) 

print(f"loinc_small data saved to {file_output_path}")