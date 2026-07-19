import numpy as np
import pandas as pd

def fill_missing(df, column, value):
    df[column] = df[column].fillna(value)

df = pd.read_csv("Cleaning_data/sales.csv")
print(df.isnull())
print(df.duplicated().sum())


fill_missing(df, "Month", "Unknown")
fill_missing(df, "Product", "MOUSE")
fill_missing(df, "Quantity", df["Quantity"].mean())
fill_missing(df, "UnitPrice", df["UnitPrice"].median())
fill_missing(df, "TotalSales", df["TotalSales"].fillna(0))
print(df.to_string())
