import pandas as pd

data = {
    "Name": ["Anuj", "Rahul", "Amit", "Neha"],
    "Marks": [85, 92, 67, 74],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

#apply() → run function on each value (powerful)

def grade(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m>=60:
        return "C"
    elif m>=40:
        return "D"
    else:
        return "Next year aana"
    
df["Grade"] = df["Marks"].apply(grade)
print(df)

#lambda → short inline function

df["Pass"] = df["Marks"].apply(lambda x: "Yes" if x >= 70 else "No")
print(df)


#map() → replace values (fast)  Converts categories into numbers (encoding)

city_map = {
    "Delhi": 0,
    "Mumbai": 1,
    "Pune": 2
}

df["City_Code"] = df["City"].map(city_map)

print(df)
