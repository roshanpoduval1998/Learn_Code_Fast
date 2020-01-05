def array_division():
        l=[]
        c=[]
        x=int(input("Enter the range of list: "))
        for i in range(0,x):
                a=int(input("enter the values : "))
                l.insert(i,a)
                i+=1
        print(l)
        for j in range(0,x):
                b=int(input("enter the values : "))
                c.insert(j,b)
                j+=1
        print(c)
        e=[]
        for z in range(0,x):
                v=l[z]/c[z]
                d=int(round(v))
                e.insert(z,d)
                z+=1
        Array=tuple(e)       
        print("Final list is {}".format(Array))
        
array_division()
