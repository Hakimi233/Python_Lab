# import pandas as pd
# # Creating Series
# # 1. Series from list
# Num = [10 , 20 , 30 ,40 ,50,60]
# series = pd.Series(Num, index = ["a", "b", "c", "d", "e", "f"])
# #print(series)

# # 2. series from dictionary
# data = {
#     "Farzana" : 95,
#     "malika" : 90,
#     "Maryam" : 85,
#     "Ali": 96
# }
# series = pd.Series(data)
# #print(series)


# # Creating DataFrame
# # 1. DataFrame from dictionary
# Data = {
#     "Name" : ["Farzana", "Marzia", "Maryam"],
#     "Grade": [96, 90, 92],
#     "Age": [25, 24, 26]
# }
# df = pd.DataFrame(Data)
# #print(df)



# # 2. DtaFrame from list of lists
# data = [
#         ["Farzana", 98],
#         ["Karima", 90],
#         ["Shirin", 93]     
# ]
# Df = pd.DataFrame(data, columns = ["Name", "Grade"])
# #print(Df)




# # 3. DataFrame from list of dictionaries
# data = [
#     {"Name": "Farzana", "Marks" : 98},
#     {"Name": "Marzia", "Marks" : 90},
#     {"Name": "Shirin", "Marks" : 94}
# ]
# df = pd.DataFrame(data)
# #print(df)



# # Filtering the data 

# Nums = [10 , 20 , 30 ,40 ,50,60]
# series = pd.Series(Nums)
# print(series[(series >= 40) & (series <= 50)])



import pandas as pd

data = {
    "Department": ["CS", "CS", "Math", "Math"],
    "Gender": ["Female", "Male", "Female", "Male"],
    "Marks": [90, 80, 85, 70]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print(pivot)
