class Shape:
    def area(self):
        return 0

width,length = input("").split()

class Rectangle(Shape):
    def area(length,width):
        return length*width
    

area1 = Rectangle()


print(area1.area())