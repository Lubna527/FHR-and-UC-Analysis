import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    data['Time_sec'] = data['Time(ms)'] / 1000
    return data
