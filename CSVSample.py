# A sample program to read data from .CSV files

import pandas as pd

data = pd.read_csv('population.csv')

# Print all values
print(data)

# Print only the first few values
print("Enter the number of initial values to display: ")
firstn = int(input())
print(data.head(firstn))

# Display all columns

