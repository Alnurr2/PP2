import math

h = int(input("Number of sides: "))
b = int(input("Input the length of a side: "))
d = 4*math.tan(180/h)
area = ((b**2)*h)/d
print(f'The area of the polygon: {area}')
print(math.tan(45))