# finding minimum number from a list and printing its sqaure

class Min():

    def __init__(self,x):

        self.x = x
        self.y = min(x)
        self.z = min(x)**2

    def rem(self):
        return "maximum is {} ".format(int(self.y))

    def rem1(self):
        return "& sqaure of minimum number is {}.".format(int(self.z))

x = [1,2,-3,4,-5,-4,-2]
a = Min(x)
print(a.rem(),a.rem1())




