import numpy as np
import pandas as pd

def fill_missing(df, column,value ):
    df[column] = df[column].fillna(value)

df = pd.read_csv("Cleaning_data/students.csv")


df["Physics"] = pd.to_numeric(df["Physics"], errors="coerce")

print(df.isnull())

# NOW check for invalid data 
print(df[(df["Age"] < 0) | (df["Age"] > 100)])
print(df[(df["StudyHours"] < 0) | (df["StudyHours"] > 24)])
print(df[(df["Attendance"] < 0) | (df["Attendance"] > 100)])
print(df[(df["Math"] < 0) | (df["Math"] > 100)])


# NOW replace them with nan
df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = np.nan
df.loc[(df["StudyHours"] < 0) | (df["StudyHours"] > 24), "StudyHours"] = np.nan
df.loc[(df["Attendance"] < 0) | (df["Attendance"] > 100), "Attendance"] = np.nan
df.loc[(df["Math"] < 0) | (df["Math"] > 100), "Math"] = np.nan


fill_missing(df, "Name", "Unknown")
fill_missing(df, "Gender", "No Gender" )
fill_missing(df, "Department", "Chimistry")
fill_missing(df, "Age", df["Age"]. mean())
fill_missing(df, "StudyHours", df["StudyHours"]. median())
fill_missing(df, "Attendance", df["Attendance"].mean())
fill_missing(df, "Math", df["Math"]. median())
fill_missing(df, "Physics", df["Physics"].median())
fill_missing(df, "Programming", df["Programming"].median())
df["Average"] = (df["Math"] + df["Physics"] + df["Programming"]) / 3
df["Gender"] = df["Gender"].replace("Male", "M")
df["Gender"] = df["Gender"].replace("X", "No Gender")

df = df.drop_duplicates()

print(df.to_string())


df.to_csv("Student _data_cleaned.csv", index=False)






