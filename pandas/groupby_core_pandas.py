import pandas as pd

data = {
    "Name": ["Anuj","Rahul","Priya","Karan","Sneha","Amit"],
    "Department": ["IT","IT","HR","HR","IT","HR"],
    "Salary": [50000,60000,45000,40000,55000,42000]
}

df = pd.DataFrame(data)
# print(df)

# It groups similar rows together and then performs calculation on each group.

# print(df.groupby("Department"))


# 1. mean() → Average per group

print(df.groupby("Department")["Salary"].mean())  #“Average salary in each department”


# sum() → Total per group

print(df.groupby("Department")["Salary"].sum())


# count() → Number of records

print(df.groupby("Department")["Salary"].count())

