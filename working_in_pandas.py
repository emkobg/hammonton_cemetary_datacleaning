import pandas as pd 
import datetime as dt
import matplotlib as mt

#Read both DataFrames 
df0 = pd.read_csv("Graveyard Data - Sheet1.csv", sep = ',')
df1 = pd.read_csv("/Users/Bobev/Desktop/Python/Data(1)/Data/halloween2019a.csv", sep = ',')

# Rename the columns in our existing DataFrame df0 
df0.rename(columns={'Number': 'ID','First Name': 'FirstName','Last Name':'LastName','Year of Birth':'DOB','Year of Death':'DOD'}, inplace=True)

#The column I had for 'Year of Birth' had a wierd spacing and python wasn't modifing it with the previous command.
df0.rename(columns={'Year of Birth ':'DOB'}, inplace=True)

#I had a columns that didn't match the previous year data frame and wasn't really necesarry 
df0 = df0.drop(df0.columns[[0,5,6]], axis=1)

#My df0 has no MiddleName so I will attempt to add it. We didn't collect middle initial, so we called them NaN 
df0.insert(loc=1, column = 'MiddleName',value = 'NaN', allow_duplicates = False)


#Time to merge both data frames into df2
result = [df0, df1]
df2 = pd.concat(result)
#print(df2)

#I've noticed some of the dates are incorrect format, so I am simply going to delete them 
df2 = df2[pd.to_datetime(df2['DOB'], errors='coerce').notna()]
df2 = df2[pd.to_datetime(df2['DOD'], errors='coerce').notna()]

#Since we have mixed date time formats that have the day,month and year of Birth/Death I am going to attempt to trim it only to the year
#Step1. convert the column to datetime : 

df2['DOB'] = pd.to_datetime(df2['DOB']).dt.year
df2['DOD'] = pd.to_datetime(df2['DOD']).dt.year

#Step2. extract the year or the month using DatetimeIndex() method 
#pd. DatetimeIndex(df2['DOB']).year
#pd. DatetimeIndex(df2['DOD']).year


df= df2.hist(('DOB'), ('DOD'))

age = ['DOD'-'DOB']
df2['Age'] = age
print (df2)

#Since my data frame has 
#desc = df0.describe()
#print (desc)

#nulls = df0.isna()
#print (nulls)