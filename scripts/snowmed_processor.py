import polars as pl
from pathlib import Path

file_path = Path('input/sct2_Description_Full-en_US1000124_20250901.txt')

df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'snomed_ct_cleaned.csv'

df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
print(f"Language codes: {df['languageCode'].unique().to_list()}")

df = df.drop(['effectiveTime', 'active', 'moduleId',
              'conceptId', 'languageCode', 'typeId', 
              'caseSignificanceId'])

df = df.with_columns(pl.lit('2025-09-01').alias('last_updated'))

df = df.rename({'id': 'code', 'term': 'description', 
                'last_updated': 'last_updated'})

df = df.unique(subset=['code', 'description'])

df = df.select(['code', 'description', 'last_updated'])

df.write_csv(output_dir / 'snomed_ct_cleaned.csv')

print(f"\nCleaned dataset shape: {df.shape}")
print(f"saved cleaned SNOMED CT data to {output_dir / 'snomed_ct_cleaned.csv'}")

print(f"\nFirst 5 rows of cleaned data:")
print(df.head())
print(f"\nMemory usage of cleaned data (MB): {df.estimated_size() / 1024**2:.2f}")


# Save a smaller sample for GitHub (e.g. first 10k rows)
df.head(10_000).write_csv(output_dir / "snomed_ct_cleaned_sample.csv")








