"""
Description: Introduction to Import Statements and File I/O
Author: Nathan
Date: January 2024
Usage: To execute, press the play button in the VSC IDE.
"""
# IMPORT STATEMENTS
import math
from math import sqrt
import random
from pprint import pprint

# Variables used in this demonstration
radius = 12.5
square = 144
fruits = ["apple", "banana", "cherry"]

# USING IMPORTED MODULES
area = math.pi * radius ** 2

root = sqrt(square)

# RANDOM
print(random.random())

print(random.randint(1, 6))

print(random.choice(fruits))

random.shuffle(fruits)
print(fruits)

# FILE I/O
"""
# reading the file only
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Writing to a file
file = open("output.txt", "w")
file.write("Hello world!")
file.close()
"""

# WITH CLAUSE
with open("example.txt", "r") as file:
    content = file.read()
    print(content)




# READ INTO DICTIONARY
data = {}
with open("dict_example.txt", "r") as input_file:
    for line in input_file:
        key, value = line.strip().split('*')
        data[key] = int(value)

print(data)
pprint(data)

