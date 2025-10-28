# Area of a Circle
import math

radius = float(input("Enter radius: "))

# Formula: π × r²
area = math.pi * (radius ** 2)
print("Area of circle is:", round(area, 2))