#1
pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

#2
Height = float(input("Height of trapezoid: "))
base_1_value = float(input('Base first value: '))
base_2_value= float(input('Base second value: '))
area = ((base_1_value + base_2_value) / 2) * Height
print("Expected Output: ", area)

#3
from math import tan, pi
n = int(input("Input number of n: "))
s = float(input("Input the length : "))
p = n * (s ** 2) / (4 * tan(pi / n))
print("The area of the polygon is: ",p)

#4
length_of_base = float(input('Length of base: '))
height_of_parallelogram = float(input('Measurement of height: '))
area = length_of_base * height_of_parallelogram
print("Area is: ", area)
