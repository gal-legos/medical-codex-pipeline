## import input/icd102019syst_codes.txt file as pandas df

import pandas as pd

file_path = 'input/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

df = df.drop(columns=['level', 'type', 'usage', 'sort', 'parent',
                      'display_code', 'icd10_code', 'parent_title',
                      'detailed_title', 'definition', 'mortality_code', 'morbidity_code1',
                      'morbidity_code2', 'morbidity_code3', 'morbidity_code4'])

df['last_updated'] = '2025-09-01' 

df = df.rename(columns={'code': 'code', 
                        'title_en': 'description',
                        'last_updated': 'last_updated'})

output_path = 'output/icd102019syst_codes.csv'
df.to_csv(output_path, index=False)
