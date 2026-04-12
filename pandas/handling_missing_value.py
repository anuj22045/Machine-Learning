# Handling Missing Values (NaN)
# Handling missing data is called Imputation in Machine Learning
import pandas as pd
import numpy as np
data = {
    "Name": ["Anuj", "Rahul", "Amit", "Neha"],
    "Age": [21, np.nan, 23, np.nan],
    "Marks": [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)
# print(df)
# print("\n\n")
# print(df.isnull()) #it will return true for the missing values and false for the non missing values
# print("\n\n")
# print(df.isnull().sum()) #it will return the count of missing values in each column

# print("\n\n")

# print(df.dropna(how="all")) #it will drop the rows where all the values are missing

df["Age"] = df["Age"].fillna(df["Age"].mean()) #eplace missing Age with average age
print(df)

print("\n\n")

df["Marks"] = df["Marks"].fillna(df["Marks"].median()) #replace missing Marks with median marks
print(df)

print("\n\n")

df["Name"] = df["Name"].fillna(df["Name"].mode()[0]) #replace missing Name with mode name
print(df)

