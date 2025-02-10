"""
Description: This Python file contains exercises designed to practice fundamental programming concepts,
             such as operators, and to learn the different types. It is part of the
             "30 Days of Python Programming" challenge.

Author: Andres Vanegas
Date: 04/02/2025
Last actualization: 10/02/2025
"""


# === Variable declaration with specific data types ===
age = int(input("Insert your age: "))
hight = float(input("Insert your high: "))

print(f"Your age it's: {age}")
print(f"Your high it's: {hight}")

# === Declare a complex number variable ===
complex_number = 3 + 4j

# === Calculate the area of a triangle ===
base = int(input(" Enter the base of the triangle: "));
height_triangle = int(input(" Enter the height of the triangle: "));
area_triangle = (0.5 * base * height_triangle)
print(f"The area of the triangle is: {area_triangle}")

# === Calculate the area and perimeter of a triangle ===
side_a = int(input(" Enter the side a of the triangle: "));
side_b = int(input(" Enter the side b of the triangle: "));
perimeter_triangle = (side_a + base + side_b)
print(f"The perimeter of triangle it's: {perimeter_triangle}")

# === Calculate the perimeter of a rectangle ===
width = int(input(" Enter the width of the rectangle: "));
height_rectangle = int(input(" Enter the height of the rectangle: "));
area_rectangle = (width * height_rectangle)
perimeter_rectangle = (2 * (width + height_rectangle))

print(f"The area of the rectangle is: {area_rectangle}")
print(f"The perimeter of rectangle it's: {perimeter_rectangle}")

# === Calculate the area and circumference of a circle ===
radius = int(input(" Enter the radius of the circle: "));
area_circle =3.14 * radius**2
circumference = 2 * 3.14 * radius

print(f"The area of the circle it's: {area_circle}")
print(f"The circumference of the circle is: {circumference}")

# === Calculate the slope, x-intercept, and y-intercept of y = 2x - 2 ===
m = 2       # Slope
b = -2      # Interception with y-axis

# Calculate the x-intercept (when y = 0)
x_intersection = -b / m  # x = -b/m

print(f"Slope (m): {m}")
print(f"y-intercept: (0, {b})")
print(f"x-intercept: ({x_intersection}, 0)")

# === Find the slope and Euclidean distance between (2,2) and (6,10) ===
euclidean_distance = ((2-6)**2 + (2-10)**2)**0.5;
slope = ((10-2)/(6-2))

print(f"Euclidean distance between (2,2) and (6,10): {euclidean_distance}")
print(f"Slope between (2,2) and (6,10) is: {slope}")

# === Compare slopes ===
comparison = slope >= m
print(f"Slope for point 9 i'ts grater than or equal to 8?: {comparison}")

# === Calculate the value of y (y = x^2 + 6x + 9) for x = -3 ===
x = -3
y = x**2 + 6*x + 9
print(f"For x = -3, the value of y  is: {y}")

# === Find the length of 'python' and 'dragon' and compare them ===
python_len = len("python")
dragon_len = len("dragon")

print(f"Are the lengths of 'python' and 'dragon' different? {python_len != dragon_len}")

# === Check if 'on' is in both 'python' and 'dragon' ===
python = "python"
dragon = "dragon"
print("'on' found in both words? ", "on" in "python" and "on" in "dragon")

# === 'I hope this course is not full of jargon.' Check if jargon is in the sentence. ===
phrase = "I hope this course is not full of jargon"
print("jargon" in phrase)

# === Check if 'on' is missing in both 'python' and 'dragon' ===
print("'on' is missing in both words? ", "on" not in "python" and "on" not in "dragon")

# === Find the length of the word 'python', convert to float, then to string ===
print(str(float(len(python))))

# === Check if a number is even or odd ===
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# === Check if the floor division of 7 by 3 is equal to the int conversion of 2.7 ===
print(f"Is 7//3 equal to int(2.7)? {7 // 3 == int(2.7)}")

# === Check if type of '10' is equal to type of 10 ===
print(type('10') == type(10))

# === Check if int(9.8) is equal to 10 ===
print(f"Is int(9.8) equal to 10? {int(9.8) == 10}")

# === Check your weekly earning ===
hours = float(input("Enter the number of hours worked in the week: "))
rate = float(input("Enter the rate per hour: "))
payment = hours * rate
print(f"Your weekly earning is: {payment}")

# === Calculate the your age in seconds "literally" ===
years = int(input("Enter the number of years you have lived: ")) < 100
second_conversion = years * 365 * 24 * 60 * 60

#=== Script to display the following table ===
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

M1 = [[1,1,1,1,1], 
      [2,1,2,4,8],
      [3,1,3,9,27],
      [4,1,4,16,64], 
      [5,1,5,25,125]]
for row in M1:
    print(row)

for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")
