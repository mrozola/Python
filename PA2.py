""""
Author: Ola Mroz
Program: - PA-2 Loops program
Last date modified: 02/03/2022

The purpose of this program is to 
predict population growth of organisms.

"""
#Input
organisms = int(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the rate of growth (a real number > 1): "))
hours_to_grow = int(input("Enter the number of hours to achieve the rate of growth: "))
total_hours = int(input("Enter the total hours of growth: "))

#for loop to get results

rate = total_hours // hours_to_grow

for round in range(rate):
    organisms = organisms * growth_rate

#Print the results
print("The total population is ", organisms)

