class Square():

	def __init__(self,x,n):

		self.x = x
		self.n = n
		self.power = (x ** n)

x = int(input("Enter the number:: "))
n = int(input("Enter the power:: "))

print(Square(x,n).power)