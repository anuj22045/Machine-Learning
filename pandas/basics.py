import pandas as pd
import numpy as np

np.arange(0, 20).reshape(5,4)

df = pd.DataFrame(data = np.arange(0, 20).reshape(5,4), index=["row1","row2","row3","row4","row5"], columns=["col1","col2","col3","col4"])


# print(df)

# top5 = df.head()
# print(top5)  #it will return the fisrt 5 rows

# last5 = df.tail()
# print(last5)

# $it returnt the types 
# type = type(df)  #type sof data structure
# print(type)

# info = df.info()
# print(info)

# des = df.describe() #Shows column types & missing values.
# print(des)


# ----------------------------------------------indexing ------------------------------------

# by using column index name 

# access3col = df[["col1", "col2", "col3"]]
# print(access3col)

#by using row index name

# accessrow = df.loc[["row1", "row2"]]
# print(accessrow)


#index location access specific rows and columns (iloc)

accessRowsCol = df.iloc[2:4,0:2] #it will return row 2 and 3 and column 0 and 1
# print(accessRowsCol)

accessRowsCol2 = df.iloc[0:3, [0,3]] #it will return row 0,1,2 and column 0,3 only , means the specific column you can access
# print(accessRowsCol2)

#convert dataframe to array

array  = df.iloc[:, 1:].values #it will return all rows and column 1,2,3 in array form
# print(array)




# ---------------------------------------basics operations-----------------------------------

df = pd.DataFrame([[1, np.nan, 2], [3, 4, 5]], index=["row1","row2"], columns=["col1","col2","col3"])

# checkNull = df.isnull() # it will return a dataframe with boolean values where True indicates the presence of NaN (missing) values and False indicates non-missing values.
# print(checkNull)

# exactnull  = df[~df.isnull()]
# print(exactnull) # it will return a dataframe where the NaN values are replaced with False and non-NaN values are replaced with True. The ~ operator is used to invert the boolean values, so that NaN values become False and non-NaN values become True.

# column me kitne different value hai it shows the value kitne baar present hai 
# df["col3"].value_counts()
print(df["col3"].value_counts())  # it will return a Series containing counts of unique values in the specified column. 

print(df["col2"].unique()) # it will return an array of unique values present in the specified column.

print(df>2)