"""
Description: Introduction to Loops
Author: Nathan
Date: February 2024
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
fruits = ["apple", "orange", "banana", "cherry"]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# FOR LOOP
print(fruits)
# iterate through a collection (list of fruit):
for fruit in fruits:
    print(fruit)

for i in range(10):
    print(i)

for i in range(2, 8):
    print(i)

for i in range(1, 100, 6):
    print(i)

for i in range(-10, 0):
    print(i)


# INPUT FUNCTION



# print(f"Name: {name} \nSalary: ${salary:,.2f}")


# WHILE LOOP


# LOOP CONTROL STATEMENTS
# CONTINUE:
"""
for number in range(1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:
        continue
    # Print all other integers
    print(number)
"""

#BREAK:
"""
# Use a for loop to iterate over the range of integers 
for number in range(1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5:
        break
    # Print all other integers.
    print(number)
"""

# INFINITE LOOP
# <ctrl> + c (in the terminal window) to stop an infinite loop in VS Code.


# NESTED LOOP
# matrix variable defined at top of editor.
