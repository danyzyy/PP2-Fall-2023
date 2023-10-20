class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
        
    
    def area(self):
        print(self.length*self.width)
        
        


task_shape=Shape
task_rectangle=Rectangle
length=int(input())
width=int(input())
task_rectangle.area(task_rectangle(length,width))
