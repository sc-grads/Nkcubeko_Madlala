#################################
## Pandas DataFrames
## Filtering Datasets
#################################

## Importing pandas and create a data frame
import pandas as pd

data = [['Dan', 30, 40000], ['John', 40, 50000], ['Helen', 35, 60000], ['Marry', 29, 58000]]

# no. of columns must match the no of columns or error
df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])

## Returning a Series of Booleans, True for each row where salary is less than 50000
df['Salary'] < 50000  # we see how the last 2 rows met our condition

# 0    False
# 1    False
# 2     True
# 3     True
# Name: Salary, dtype: bool

## Selecting and returning all rows where salary is less than 50000. This is a condition based on a column.
df[df['Salary'] < 50000]

## Using the loc[] method with the same result
df[df.loc[:, 'Salary'] < 50000]
#  Name   Age    Salary
# 0    Dan    30 40000

## maximum and minimum of all values in a column.
df['Salary'].max()  # => 60000
df['Age'].min()  # => 29

## idxmax() returns the index of the row where the Salary column has the maximum value.
r = df['Salary'].idxmax()
print(r)  # => 2

df.iloc[r]
# Name      Helen
# Age          35
# Salary    60000
# Name: 2, dtype: object


## Changing the default index and use another column as index
df.set_index('Salary', inplace=True)
print(df)
# Name Age
# Salary
# 40000    Dan    30
# 50000    John   40
# 60000    Helen  35
# 58000    Marry  29

## The index column doesn't count when getting a column using its index
df.iloc[0, 0]  # => 'Dan'

## If you want to get and return a value using df.loc[] by key, you use the new key which is Salary
df.loc[40000, 'Age']  # => 30

## Resetting the index to its initial value
df.reset_index(inplace=True)

## Checking on multiple conditions. AND Aperator
df[(df['Salary'] > 50000) & (df['Age'] > 30)]
#  Salary Name   Age
# 2    60000  Helen  35

## Using the OR Operator
df[(df['Salary'] > 50000) | (df['Age'] < 30)]
# Salary   Name   Age
# 2    60000  Helen  35
# 3    58000  Marry  29


## Returning values that fall within a specific range.
df[df['Salary'].between(45000, 59000)]  # the arguments are inclusive
#  Salary Name   Age
# 1    50000  John   40
# 3    58000  Marry  29
