# ml_utils.py

import pandas as pd

def add_features(df):
    df = df.copy()
    df["AvgChargesPerMonth"] = df["TotalCharges"] / (df["tenure"] + 1)
    df["ServiceCount"] = df[["PhoneService", "MultipleLines", "OnlineSecurity", 
                             "OnlineBackup", "DeviceProtection", "TechSupport", 
                             "StreamingTV", "StreamingMovies"]].apply(
                             lambda row: sum(val == "Yes" for val in row), axis=1)
    df["HasStreaming"] = df[["StreamingTV", "StreamingMovies"]].apply(
                             lambda row: any(val == "Yes" for val in row), axis=1)
    return df
