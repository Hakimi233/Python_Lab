import pandas as pd

# Series - is  a one- dimensional labeled array 
# Loc - use to access elements by index label
# iloc - use to access elements by index position

# data = [100, 102, 105, 200, 300, 250]
# series = pd.Series(data, index = ["A", "B", "C", "D", "E", "F"])
# series.loc["B"] = 140
# print(series)
# print(series.iloc[0])
# print(series[series > 200])


# calories = {"day1" : 430, "day2": 450, "day3": 500}
# series = pd.Series(calories)
# print(series)


# Names = ["Bulbasaur", "lvysaur", "Venusaur", "Charmander", "Chrmeleon", "Charizard"]
# series = pd.Series(Names, index = [1, 2 ,3 ,4 ,5,6])
# print(series)



# DataFrame - is a two-dimensional array

# dic = {
#     "Name" : ["Farzana", "Amina", "fatima","Mina"],
#     "Age" : [20, 25, 33, 30 ]
# }
# df = pd.DataFrame(dic, index = ["Employee1", "Employee2", "Employee3", "Employee4"])
# print(df.loc["Employee2"])
# print(df.iloc[3])

# # Adding new column
# df["Job"] = ["Engineer", "Doctor", "Teacher", "Nurse"]
# print(df)

# # Adding new row
# new_row = pd.DataFrame([{"Name": "Sara", "Age": 28, "Job": "cook"}], index=["Employee5"])
# df = pd.concat([df, new_row])
# print(df) 




# importing the file and using to_string() to print the entire DataFrame


# df = pd.read_csv("Data.csv", index_col = "Name")
# print(df.to_string())  the file and using to_string() to print the entire DataFrame

# Selection by column
#print(df[["Name", "StudentID"]].to_string())


# Selection by row
# print(df.loc["Rahim"])
# print(df.iloc[1:3])



# DATA CLEANING 
# df = pd.read_csv("Data.csv")


# 1. Drop irrelevant columns
# df = df.drop(columns=["Average"])
# print(df.to_string())


# 2. Handling missing values
# df = df.dropna(subset= ["Age"])
# print(df.to_string())
# print ( df . isnull () )
# print ( df . isnull () .sum () )

# 3. replacing missing values
#df = df.fillna({"Age": "None"})

# 4. Removing duplicates
# df = df.drop_duplicates()
# print(df.to_string())



df = pd.read_csv("Data.csv")
# print(df.to_string()) 
print(df.isnull().sum())
# print(df.dropna()) ------------ is used to remove rows with missing values
#print(df.fillna(5))
print(df.isnull())
df["Name"] = df["Name"].fillna("Unknown")
print(df)

