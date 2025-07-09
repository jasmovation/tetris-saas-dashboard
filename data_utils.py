import pandas as pd

def load_and_transform_data(filepath="dashboard_data.csv", sample_size=200):
    df = pd.read_csv(filepath)
    return df.sample(n=sample_size)
