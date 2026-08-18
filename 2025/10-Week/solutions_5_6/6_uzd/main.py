# main.py
from geometry import *

circle_radius = 5
print(f"Apļa laukums: {circle_area(circle_radius)}")
print(f"Apļa perimetrs: {circle_perimeter(circle_radius)}")

length = 10
width = 5
print(f"Taisnstūra laukums: {rectangle_area(length, width)}")
print(f"Taisnstūra perimetrs: {rectangle_perimeter(length, width)}")

base = 8
height = 5
side1, side2, side3 = 5, 7, 8
print(f"Trijstūra laukums: {triangle_area(base, height)}")
print(f"Trijstūra perimetrs: {triangle_perimeter(side1, side2, side3)}")

square_side = 4
print(f"Kvadrāta laukums: {square_area(square_side)}")
print(f"Kvadrāta perimetrs: {square_perimeter(square_side)}")
