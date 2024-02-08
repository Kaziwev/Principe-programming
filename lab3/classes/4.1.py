class Rectangle:
    int =0
    intk=0
    k=0
    l=0
    dist=0
    dist1=0
class Shape(Rectangle):
    def get_Int(Shape):
        Shape.int=int(input())
        Shape.intk=int(input())
    def printk(Shape):
        print(Shape.int, Shape.intk)
    def za(Shape):
        Shape.k=int(input())
        Shape.l=int(input())   
    def move(Shape):
        print(Shape.int+Shape.k, Shape.intk+Shape.l)
    def compute(Shape):
        Shape.dist=int(input())
        Shape.dist1=int(input())
    def dikta(Shape):
        print(Shape.int-Shape.dist, Shape.intk-Shape.dist1)
obj=Shape()
obj.get_Int()
obj.printk()
obj.za()
obj.move()
obj.compute()
obj.dikta()
