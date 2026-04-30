import pandas as pd
import numpy as np

def load_data(path, country):
    df = pd.read_csv(path)
    df["Country"] = country
    return df


def convert_date(df):
    df["DATE"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")
    df["Month"] = df["DATE"].dt.month
    return df
