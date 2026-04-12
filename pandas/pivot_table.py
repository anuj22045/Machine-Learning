# It summarizes data into a matrix / report format
import pandas as pd

data = {
    "Name": ["Anuj","Rahul","Priya","Karan","Sneha","Amit"],
    "Department": ["IT","IT","HR","HR","IT","HR"],
    "Gender": ["M","M","F","M","F","M"],
    "Salary": [50000,60000,45000,40000,55000,42000]
}

df = pd.DataFrame(data)
# print(df)

# basic pivot table 

# print(pd.pivot_table(df, values="Salary", index = "Department"))

# Add Columns (Real Pivot Power ⭐)
# print(pd.pivot_table(df, values="Salary", index="Department", columns="Gender"))

mul = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc=["mean","max","min","count"]
)

print(mul)

replace_0 = pd.pivot_table(df, values="Salary", index="Department", columns="Gender", fill_value=0)

print(replace_0)