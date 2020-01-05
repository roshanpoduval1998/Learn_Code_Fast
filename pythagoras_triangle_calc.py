def pythagoras():
        import math
        i=int(input("calculate the hypotenuse \n Enter the side of first triangle : "))
        j=int(input(" Enter the side of second triangle : "))
        k=int((i*i)+(j*j))
        c=math.sqrt(k)
        d=(round(c,4))
        print("Hypotenuse is {}. ".format(d))
        print("Hypotenuse calculated")
pythagoras()
        
