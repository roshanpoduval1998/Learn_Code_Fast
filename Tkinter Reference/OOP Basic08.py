class Vowels():

	def __init__(self,x):

		self.x = x
		self.z = list(x)

	def vowels_finder(self):
		z = []
		c = []
		for i in self.x:
			if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
				z.append(i)
			else:
				c.append(i)
		return "vowels are {} and consonants are {}".format(z,c)

x = "abcde"
a = Vowels(x)
print(a.vowels_finder())