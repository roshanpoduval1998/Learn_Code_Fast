def printnumber(x):
    for i in range(1,x+1):
        a = []
        for j in range(i):
            a.append(i)
            j=a
        print(j)

def printnumbersquare(x):
    for i in range(1,x+1):
        a = []
        for j in range(i):
            a.append(i**2)
            j=a
        print(j)

def printnumbercube(x):
    for i in range(1,x+1):
        a = []
        for j in range(i):
            a.append(i**3)
            j=a
        print(j)
        
x = int(input("How many lines do you need ? \n"))
printnumber(x)
printnumbersquare(x)
printnumbercube(x)
