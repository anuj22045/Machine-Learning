import pandas as pd

data = {
    "Name": ["Anuj", "Rahul", "Amit", "Neha", "Riya", "Rahul", "Anuj"],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Mumbai", "Delhi"],
    "Marks": [85, 90, 70, 88, 60, 90, 85]
}

df = pd.DataFrame(data)

print(df["City"].unique())  #Use when you want to know categories present return all unique cities

print(df["Name"].unique())

print(df["City"].nunique()) #return the numbr   of uniques cities 

print(df["Name"].value_counts()) #return the count occurance of each category


