import math

number = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

a = (number * length**2) / (4 * math.tan(math.pi / number))

print("The area of the polygon is:", a)