"""
Author:Ola Mroz 
Program: - PA-1 BMI calculator
Last date modified: 01/26/2022

The purpose of thie program is to compute an 
individual's Body Mass Index (BMI) based on their 
height (inches) and weight (pounds). 
"""
#Conversions
KG_CONVER = 0.45
M_CONVER = 0.0254

#Get user's weight in lbs and height in inches
lbs = float(input("Please enter your weight in lbs "))
inches = float(input("Please enter your height in inches "))

#Convert the wight from lbs to kg and height from inches to meters
weight = lbs * KG_CONVER
height = inches * M_CONVER

#Calculate BMI
bmi = round(weight/(height**2), 2)

#Output user's BMI
print("Your BMI is ", bmi)