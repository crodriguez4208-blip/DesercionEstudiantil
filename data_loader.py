import pandas as pd

def load_data(path="students.csv"):
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} student records.")
    return df
