"""
Description: This Python file contains exercises designed to practice fundamental programming concepts 
             such as variables, data types, operators, and built-in functions. It is part of the 
             "30 Days of Python Programming" challenge.

Author: Andres Vanegas
Date: March 2, 2025
"""

# Day 2: 30 Days of Python Programming - First Part of Exercises

# Variable Declarations
first_name = "Andres"                       # String
last_name = "Vanegas"                       # String
full_name = first_name + " " + last_name    # Concatenated String
country = "Colombia"                        # String
city = "Bogota"                             # String
age = 20                                    # Integer
year = 2025                                 # Integer
is_married = False                          # Boolean
is_true = True                              # Boolean
is_light_on = True                          # Boolean

# Length Comparison of Variables
first_name_len = len(first_name)
last_name_len = len(last_name)
comparison = first_name_len >= last_name_len
print(f"Is the length of the first name greater than or equal to the last name? {comparison}")

# Multiple Variables Assigned in One Line
pelicula, genero, duracion, calificacion, recomendable = "Paddington", "Infantil", 222, 6.2, True
print(f"Movie: {pelicula}, Genre: {genero}, Duration: {duracion} mins, Rating: {calificacion}, Recommended: {recomendable}")

# Day 2: 30 Days of Python Programming - Second Part of Exercises

# Type and Length Information
variables = (pelicula, genero, first_name, last_name, country, city, str(year))
print("Variable Types:", [type(var) for var in variables])
print("Variable Lengths:", [len(str(var)) for var in variables])

# Arithmetic Operations
num_one = 5
num_two = 4

total = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exponent = num_one ** num_two
floor_division = num_one // num_two

# Print Arithmetic Results
print(f"Addition: {total}")
print(f"Subtraction: {difference}")
print(f"Multiplication: {product}")
print(f"Division: {division}")
print(f"Remainder: {remainder}")
print(f"Exponent: {exponent}")
print(f"Floor Division: {floor_division}")

# Circle Calculations
radius = 30
area_of_circle = 3.14 * (radius ** 2)           # Area = πr²
circumference_of_circle = 2 * 3.14 * radius     # Circumference = 2πr

# Print Circle Results
print(f"The area of the circle is: {area_of_circle}")
print(f"The circumference of the circle is: {circumference_of_circle}")