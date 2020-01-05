class Cylinder():

    def __init__(self,height=1,radius=1):

        self.pi = 3.14
        self.h = int(height)
        self.r = int(radius)

    def volume(self):

        #volume of cylinder is pi*r*r*h
        volume = self.pi*(self.r**2)*self.h
        print("Volume of cylinder is {}.".format(volume))

    def surface_area(self):

        #surface area of cylinder is (2*pi*r*h)+(2*pi*r*r)
        surface_area = (2*self.pi*self.r*self.h)+(2*self.pi*(self.r**2))
        print("Surface area of cylinder is {}".format(surface_area))
try:
    x = int(input("Enter the radius of the cylinder :: "))
    y = int(input("Enter the height of the cylinder :: "))
    c = Cylinder(x,y)
    c.volume()
    c.surface_area()
except:
    print("Entered value is incorrect")

