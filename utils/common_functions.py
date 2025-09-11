# type: ignore

def save_to_formats(df, base_filename):
    """
    Save a DataFrame to multiple formats: CSV.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    base_filename (str): The base filename without extension.

    Returns:
    None
    """
    import pandas as pd

    # Save as CSV
    csv_path = f"{base_filename}.csv"
    df.to_csv(csv_path, index=False)
    print(f"DataFrame saved to {csv_path}")


