"""
Description: This Python file contains exercises designed to practice fundamental programming concepts,
             such as operators, and to learn the different types. It is part of the 
             "30 Days of Python Programming" challenge.

Author: Andres Vanegas
Date: 04/02/2025

"""


#Variable declaration with an especific data type
age = int(input())
hight = float(input())
print(f"Your Age it's: {age}")
print(f"Your high it's: {hight}")

#Calculate area triangle
base = int(input(" Enter the base of the triangle: "));
height_triangle = int(input(" Enter the height of the triangle: "));
area_triangle = (0.5 * base * height_triangle)
print(f"The area of triangle it's: {area_triangle}")

#Calculate the perimeter of a triangle
side_a = int(input(" Enter the side a of the triangle: "));
side_b = int(input(" Enter the side b of the triangle: "));
perimeter_triangle = (side_a + base + side_b)
print(f"The perimeter of triangle it's: {perimeter_triangle}")

#Calculate the area and perimeter of a rectangle 
width = int(input(" Enter the width of the rectangle: "));
height_rectangle = int(input(" Enter the height of the rectangle: "));
area_rectangle = (width * height_rectangle)
perimeter_rectangle = (2 * (width + height_rectangle))
print(f"The area of rectangle it's: {area_rectangle}")
print(f"The perimeter of rectangle it's: {perimeter_rectangle}")

#Get the radius of a circle and calculate the area and circumference
radius = int(input(" Enter the radius of the circle: "));
area_circle =3.14 * radius**2
circunference = 2 * 3.14 * radius
print(f"The area of the circle it's: {area_circle}")

#Calculate the slope, x-intercept and y-intercept of y = 2x - 2
# 0 = 2x - 2
# 2/2 = x

x = 1
y = 2 * x - 2
