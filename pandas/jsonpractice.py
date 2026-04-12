import pandas as pd
# pd.read_json('data.json')


df = pd.read_json('data.json')
# print(df)



# print(pd.read_json('data.json', orient='index'))
# print("\n\n")
# print(pd.read_json('data.json', orient='records'))
# print("\n\n")
# print(pd.read_json('data.json', orient='split'))


# -----------------------------------------JSOn orientation
df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index = ['row1', 'row2'], 
                  columns = ['col1', 'col2'])

print(df)

# #convert data frame to json file 
print("\n\n")

# print(df.to_json())  #deault orientation is columns
# print("\n\n")

# print(df.to_json(orient='index')) #data goruped by row index
# print("\n\n")
# print(df.to_json(orient='columns')) #it give preference to columns 

# print(df.to_json(orient='records')) #it give preferencw to records (meaning each row become one json objects)

# print(df.to_json(orient='table')) #it give preference to table (it give the data in the form of table)

df = pd.read_csv('wine.csv') 
# print(df.head())

# print(df.to_json(orient='records'))

print(pd.json_normalize(df.to_dict(orient='records')))