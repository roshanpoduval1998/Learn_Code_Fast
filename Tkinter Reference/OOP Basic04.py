class Triangle():

	def __init__(self,base,height,side=1):

		self.base = base
		self.height = height
		self.side = side
		self.triangle_area = base * height * 0.5
		self.square = side ** 2

x = int(input("Enter the Base:: "))
y = int(input("Enter the height:: "))
my_triangle = Triangle(x,y)
x = my_triangle.triangle_area
print("Area of Triangle = {} ".format(x))