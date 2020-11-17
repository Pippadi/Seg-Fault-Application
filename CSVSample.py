# A sample program to read data from .CSV files

import pandas as pd
import time

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
print("\nDisplaying the names of all ")
print(data.columns)

# Display a specific column
print("Enter the name of any column whose values to display: ")
cname = input()
# Display the values from the top
print(data[cname])

# Exit the program
print("\n Exiting in 5 s from now...")
# Wait for 5 seconds before exiting
time.sleep(5)
