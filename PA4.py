""""
Author: Ola Mroz
Program: - PA-4 term frequency vector program
Last date modified: 02/16/2022

The purpose of this program is to 
find the term frequency vector of a 
document stored in a text file.

"""
import re

#Input file name
file = input("Enter filename: ")
infile = open(file, 'r')

frequency = {}

#for loop to get the set of unique words and and their frequencies
for line in infile:
    for word in line.split():
        new_word = re.sub(r'[^\w\s]', '', word)
        value = str(new_word)
        value = value.lower()
        number = frequency.get(value, 0)
        if number == 0:
            frequency[value] = 1
        else:
            frequency[value] = number + 1

#find the number of unique words in the file
total = len(frequency)

#print out the results in alphabetical order
print("There are", total,"unique terms.")

dictionary_list = frequency.keys()
for word in sorted (dictionary_list):
    print(frequency[word], word)