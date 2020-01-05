x = input("enter the number in ! at the end")
z = x.split("-")
z1 = x.split("*")
z2 = x.split("/")
z3 = x.split("%")
z4 = x.split("^")
z5 = x.split("√")
z6 = x.split("(")
z7 = x.split(")")
y = z+z1+z2+z3+z4+z5+z6+z7
if len(y) >= 2 :
    if x[0] != "!":
        s = x.split("!")
        g = int(s[0])
        k = g+1
        d = []
        l = 0
        for i in range(int(g)):
            j = k - 1
            d.insert(l,j)
            k-=1
            i+=1
        z=1
        for c in list(d):
            z=z*c
        y = float(z)
        print(y)
        
            
            
