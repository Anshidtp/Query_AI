import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the resume dataset from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} resumes from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()