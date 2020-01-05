def character(x):
    num = 65
    for i in range(1,x+1):
        a = []
        for j in range(i):
            a.append(chr(num))
            j = a
        num+=1
        print(j)

def lowercasecharacter(x):
    num = 65
    for i in range(1,x+1):
        a = []
        for j in range(i):
            a.append((chr(num)).lower())
            j = a
        num+=1
        print(j)


x = int(input("How many lines of character needed ? \n"))        
character(x)
lowercasecharacter(x)
