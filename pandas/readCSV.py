import pandas as pd
from io import StringIO
df = pd.read_csv('mercedesbenz.csv')  #when it read the csv file it will convert to data frame , it change to string io

# print(df.head())

# print(type(df))  #it will show the type of data frame   




# -------------------------------------------------------
data = ('col1,col2,col3\n1,2,3\n4,5,6\n7,8,9')
# print(type(data))


#in memory file format object 
print(StringIO(data))    #StringIO converts a string into a file-like object (in memory).

# print(pd.read_csv(StringIO(data)))


#if we want to access the specific column then we can do like this 
# df = pd.read_csv('mercedesbenz.csv', usecols=['X1', 'X2', 'X3', 'X4', 'X5'])  #it will read only the column X1 and X2
# print(df.head())


# df.to_csv('test.csv', index = False)  #create a csv file with name test.csv and it will save the data frame in that file


# -----------------------------------------------datatypes in csv file --------------------------------------
# data = ('col1,col2,col3\n1,2,3\n4,5,6\n7,8,9'   )
# df = pd.read_csv(StringIO(data), dtype={'col1': 'int32', 'col2':'float64', 'col3': 'object'})
# print(df.info())


# print(df.dtypes) #check data types


# ---------------------------------------use index column and usecols ----------------------------------------

data = ('a,b,c\n'
        '4, apple, bat, \n'
        '5, orange, cow, \n')

df = pd.read_csv(StringIO(data), usecols=['b','c'], index_col=False) #it will read only the column b and c and it will not set the index column as a

print(df)