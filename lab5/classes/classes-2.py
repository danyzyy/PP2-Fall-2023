class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length=length
        
    
    def area(self):
        print(self.length**2)
        
        


task_shape=Shape
task_square=Square
length=int(input())
task_square.area(task_square(length))
