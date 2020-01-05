# class with one attributes and two methods

class Circle():

    pi = 3.14
    
    def __init__(self,radius):

        self.radius = radius

    def area_of_circle(self,number):

        area = 2 * ((self.radius)**2) * Circle.pi
        area_times = number * area
        print("Area of the circle is {}".format(area))
        print("& its {} times is {}.".format(number,area_times))

    def circumference(self):

        circumference = 2 * Circle.pi * self.radius
        print("& circumference is {}".format(circumference))

        

x = int(input("Enter the radius value:: \t"))
y = int(input("How many times the value of area you want ? \t"))
my_circle = Circle(x)
my_circle.area_of_circle(y)
my_circle.circumference()
