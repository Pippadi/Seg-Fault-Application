# A sample program to read data from .CSV files

import pandas as pd

data = pd.read_csv('population.csv')

# Print all values
print(data)

# Print only the first few values
print("Enter the number of initial values to display: ")
# Parse to integer
firstn = int(input())
# Display the values from the top
print(data.head(firstn))

# Display the names of all columns
print("Displaying the names of all ")
print(data.columns)
