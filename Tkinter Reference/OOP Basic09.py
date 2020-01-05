# passing argumment inside class method

class Weight():

	def __init__(self):
		self.a = "The Weight of the value is calculated and "

	def weigh_(self,*z):
		d = []
		j = 0
		for i in range(1,len(a)+1):
			num = i * a[j]
			d.append(num)
			i+=1
			j+=1
		return self.a + "Weighted sum is {}".format(sum(d))

x = input('Enter the value : ')
a = []
for i in x:
	a.append(int(i))

b = Weight()
print(b.weigh_(a))

