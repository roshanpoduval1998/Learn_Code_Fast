import math

class Line():

    def __init__(self,co_ordinate_1,co_ordinate_2):

        self.x1 = int(co_ordinate_1[0])
        self.x2 = int(co_ordinate_2[0])
        self.y1 = int(co_ordinate_1[1])
        self.y2 = int(co_ordinate_2[1])
        
    def distance(self):
        try:
            distance = math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2))
            print("Distance between two co-ordinate is {}".format(distance))
        except:
            pass
        
    def slope(self):
        try:
            slope = ((self.y2-self.y1)/(self.x2-self.x1))
            print("Slope of the line is {}".format(slope))
        except:
            pass
        
    def midpoint(self):
        try:
            x = (self.x1+self.x2)/2
            y = (self.y1+self.y2)/2
            z = print("Midpoint of the line is (x,y)=({},{})".format(x,y))
        except:
            pass

x = str(input("Enter the first co_ordinate in x,y format :: "))
y = str(input("Enter the second co_ordinate in x,y format :: "))

try:
    x = x.split(",")
    y = y.split(",")

    co_ordinate_1 = list(x)
    co_ordinate_2 = list(y)

    a = Line((co_ordinate_1),(co_ordinate_2))

    a.distance()
    a.slope()
    a.midpoint()  

except:
    print("Entered value is incorrect !")
    
