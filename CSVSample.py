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
#if firstn>=0:
    firstn=int(firstn)
#else:
 #   print("Error!")

# Display the values from the top
print(data.head(firstn))
# Alternative: print(data.head[1:2])

# Display the names of all columns
print("\nDisplaying the names of all ")
print(data.columns)

# Display a specific column
print("\nEnter the name of any column whose values to display (case): ")
cname = input()
# Display all values
print(data[cname])

# Display multiple columns
print("\nEnter the number of the first column (in the previously mentioned order): ")
cl1=int(input())
print("\nEnter the number of the last column (in the previously mentioned order): ")
cl2=int(input())
# Display values from cl1 to cl2
print(data[cl1:cl2])

# Exit the program
print("\n Exiting in 5 s from now...")
# Wait for 5 seconds before exiting
time.sleep(5)
