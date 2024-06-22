# Caraballo, Joseph
# 20 June 2024
# P2LAb1
# Creating a calculator program for Circle Formulas

import math

def circle_formulas():
    radius = float(input("What is the radius of the circle? "))
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2

    print(f"The diameter of the circle is: {diameter:.2f}")
    print(f"The circumference of the circle is: {circumference:.2f}")
    print(f"The area of the circle is: {area:.2f}")
circle_formulas()