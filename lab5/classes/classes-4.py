import math

class point:
    def __init__(self, point_a = 7  , point_b = 2 ):
        self.point_a  = point_a
        self.point_b  = point_b

    def show(self):
        print(f'{self.point_a}'+ ' '+ f'{self.point_b}')

    def move(self, point_a , point_b):
        self.point_a = point_a
        self.point_b = point_b
        print('Changed coordinates:',self.point_a,self.point_b)

    def dist(self,point_a,point_b):
        d = math.sqrt(pow((self.point_a - point_a),2) + pow((self.point_b - point_b),2))
        print(d)

p = point()
p.show()

p.move(7 , 8)
second_point = point(1 , 1)

second_point.show()
p.show()

p.dist(5,9)