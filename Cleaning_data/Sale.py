import pandas as pd
import numpy as np

def fill_missing(df, column, value):
    df[column] = df[column]. fillna(value)

df = pd.read_csv("Cleaning_data/sales.csv")
print(df)

# checking the invalid 
print(df[df["Quantity"] < 0])
print(df[df["UnitPrice"] < 0] )

valid_months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
print(df[~df["Month"].isin(valid_months) & df["Month"].notna()])


#Replacing with the Nan
df.loc[df["Quantity"] < 0, "Quantity"] = np.nan
df.loc[df["UnitPrice"] < 0, "UnitPrice"] =np.nan
valid_months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
df.loc[~df["Month"].isin(valid_months), "Month"] =np.nan


fill_missing(df, "Month", "Unknown")
fill_missing(df, "Product", "Unknown")
fill_missing(df, "Quantity", df["Quantity"].mean())
fill_missing(df, "UnitPrice", df["UnitPrice"]. median())

df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

print(df.to_string())

df.to_csv("Sales_data_Cleaning.csv", index=False)