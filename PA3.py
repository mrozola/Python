"""
Author: Ola Mroz 
Program: PA3 - read from file 
Last date modified: 02/12/2022

The purpose of this program is to process the file data.txt
and find the following:
•Total lines in the file
•Min
•Max
•Mean
•Missing (-1)

"""

#open the text file
file = open("data.txt")

#initialize all values
missing = 0
count = 0
total = 0
max_value = -1
min_value = -1

#loop
for line in file:
    value = float(line)
    if value == -1:
        missing += 1
        continue
    count += 1
    total += value
    if max_value == -1 or value > max_value:
        max_value = value
    if min_value == -1 or value < min_value:
        min_value = value

# calculate the mean and number of lines
mean_value = total/count
no_lines = count + missing

#output results
print("Total lines in the file: ", no_lines)
print("Min: ", min_value)
print("Max: ", max_value)
print("Mean: ", mean_value)
print("Missing: ", missing)