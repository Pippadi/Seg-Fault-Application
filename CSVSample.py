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
firstn=int(firstn))

# Display the values from the top
print(data.head(firstn))
# Alternative: print(data.head[1:2])

# Display the names of all columns
print("\nDisplaying the names of all ")
print(data.columns)

# Display a specific column
print("\nEnter the name of any column whose values to display (case): ")
cname = input()
# Display all values of that column
print(data[cname])

# Not working
# Display multiple columns
#print("\nEnter the number of the first column (in the previously mentioned order): ")
#rl1=int(input())
#print("\nEnter the number of the last column (in the previously mentioned order): ")
#rl2=int(input())
# Display values of x location
print(data['x location'])

# Display a specific row
print("\nEnter the number of any row: ")
rown=int(input())-1
# Display each row
print(data.iloc[rown])

# Exit the program
print("\n Exiting in 5 s from now...")
# Wait for 5 seconds before exiting
time.sleep(5)
