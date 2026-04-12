import pandas as pd

customers = pd.DataFrame({
    "id":[1,2,3],
    "name":["Anuj","Rahul","Priya"]
})

orders = pd.DataFrame({
    "id":[1,1,2,4],
    "product":["Laptop","Mouse","Keyboard","Mobile"]
})

# INNER JOIN (default)  (Only matching ids)

mrge = pd.merge(customers, orders, on="id")

print(mrge)

print("\n\n")


# LEFT JOIN ⭐ (most used in projects)   (Keep all customers even if no order)

left_join = pd.merge(customers, orders, on="id", how="left")
# print(left_join)

# print("\n\n")


# RIGHT JOIN
right_join = pd.merge(customers, orders, on="id", how="right")
# print(right_join)

#OUTER JOIN (Keep everything from both tables)

outer_join = pd.merge(customers, orders, on="id", how="outer")
# print(outer_join)

# ------------------------------------------------------------------------------------------------------------

# 2. concat() — Stack data  (Used when same structure but multiple files)

jan = pd.DataFrame({"sales":[10,20]})
feb = pd.DataFrame({"sales":[30,40]})

concat = pd.concat([jan,feb])  #Adds rows (vertical stacking)
print(concat)
print("\n\n")

horiz_concat = pd.concat([jan,feb], axis=1)
print(horiz_concat)

#  join() — Index based merge
