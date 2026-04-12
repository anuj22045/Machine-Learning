import pandas as pd

data = {
    "Name": ["Anuj", "Rahul", "Amit", "Neha", "Riya"],
    "Age": [21, 25, 19, 23, 25],
    "Marks": [85, 90, 70, 88, 60],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}
df = pd.DataFrame(data)
# print(df)


#single condition
# print(df[df["Age"]>21]) #it will return the rows where age is greater than 21

# #multiple conditions

# print("\n\n")

# print(df[(df["Age"]>20) & (df["Marks"]>80)]) #it will return the rows where age is greater than 20 and marks is greater than 80

# print("\n\n")

# print(df[(df["City"] == "Delhi") | (df["City"] == "Pune")])

# print("\n\n")


# print(df[df["Marks"] > 80][["Name", "Marks"]]) #it will return the name and marks of the students whose marks is greater than 80

# print("\n\n")

# print(df[df["City"] != "Delhi"]) #it will return the rows where city is not equal to Delhi


# ---------------------------------loc → label based selection---------------------------------------

print(df.loc[:, "Name"]) #it will return the name column

print("\n\n")

print(df.loc[:, ["Name", "Marks"]]) #it will return the name and marks column
print("\n\n")

# -----------------------------------------iloc → position based selection---------------------------------------

print(df.iloc[0]) #it will return the first row

print("\n\n")

# print(df)

print(df.iloc[:, 0]) #it will return the first column

print("\n\n")
print(df.iloc[2, 1]) #it will return the value at 2nd row and 1st column (age of amit)