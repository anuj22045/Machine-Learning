import pandas as pd
data = {
    "Name": ["Anuj", "Rahul", "Amit", "Rahul", "Anuj"],
    "Age": [21, 25, 19, 25, 21],
    "Marks": [85, 90, 70, 90, 85]
}

df = pd.DataFrame(data)
print(df)

# Detect Duplicates → duplicated()
print(df.duplicated()) #Returns True for duplicate rows (after first occurrence)

print("\n\n")

print(df[df.duplicated()]) #it will return the duplicate rows

print("\n\n")
# Remove Duplicates → drop_duplicates()
print(df.drop_duplicates()) #it will return the data frame with duplicate rows removed (keep first occurrence)
print("\n\n")
