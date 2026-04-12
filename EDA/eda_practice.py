import pandas as pd
# import matplotlib.pyplot as plt
df = pd.read_csv("studentdata.csv")


df.columns = df.columns.str.strip().str.lower()
#---------------------------------------------view data----------------------------------------------------
# print(df.head())

print("\n\n")

# print(df.tail())

print("\n\n")
# print(df.sample(7))  #it return the random rows

# print(df.shape)

# print(df.columns)

# print(df.info())

# print(df.nunique()) #used to count the number of unique (distinct) values in a Series

# print(df["gender"].unique())

# print(df.isnull().sum())  #it detect for missing values 

# ----------------------------------------handling the missing value ---------------------------------------------------

# print(df["math score"].fillna(df["math score"].mean(), inplace=True))  #it work like inplace of NaN it find the avg and fill the value inplace of NaN


# For text/categorical columns we use:

# mode (most frequent value) instead of mean

# print(df["test preparation course"].fillna(df["test preparation course"].mode()[0], inplace=True))


# -------------------------------------------------Duplicates records ------------------------------------------------

# print(df.duplicated().sum())  #check how many duplicates row exist 

# df.drop_duplicates(inplace=True) #This permanently deletes repeated rows.


# ------------------------------------------------------Wrong Data Types-------------------------------------------

# df["Date"] = pd.to_datetime(df["Date"]) #Convert Date column into real datetime format

# df["Age"] = df["Age"].astype(int)





# --------------------------------------Statical  understanding ----------------------------------------------

# print(df.describe()) #learn: min / max range average values abnormal numbers


#Measure Distribution (Skewness)  **** (an imbalanced dataset where the target variable or features are not uniformly distributed, causing a lopsided (asymmetrical) representation)*****
# example interpretation
# +1.2 → Most students scored LOW, few toppers
# -0.7 → Most students scored HIGH
# 0.01 → Balanced class

#range
# -0.5 to +0.5         	        Almost normal distribution (best case)
# -1 to -0.5 or +0.5 to +1    	moderately skewed
# >	strongly skewed            (problematic for ML)
# print("Math Skew:", df["math score"].skew())
# print("Reading Skew:", df["reading score"].skew())
# print("Writing Skew:", df["writing score"].skew())


# print(df.mean(numeric_only=True))  #Tells overall performance level of students (formula = sum of values / total values)
# print(df.median(numeric_only=True))  #used to find the missing value Middle value 
# print(df.mode())


# ------------------------------------------co relation matrix -------------------------------------------

# Correlation Which feature affects target variable
# How to understand this
# Correlation values range:

# Value	      Meaning
# +1	          perfect relationship
# 0	          no relationship
# -1	          opposite relationship
# corr = df.corr(numeric_only=True)   
# print(corr)

# --------------------------------------------Metplotlib ----------------------------------------


# plt.hist(df["math score"], bins=20)
# plt.title("Math Score Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.show()


# plt.boxplot(df["math score"])
# plt.title("Math Score Spread")
# plt.show()



# avg = df.groupby("gender")["math score"].mean()

# plt.bar(avg.index, avg.values)
# plt.title("Average Math Score by Gender")
# plt.xlabel("Gender")
# plt.ylabel("Average Marks")
# plt.show()