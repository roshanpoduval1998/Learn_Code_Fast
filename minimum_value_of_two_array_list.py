def minimum_value_array_list():
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
                if l[z]<c[z]:
                        e.append(l[z])
                elif c[z]<l[z]:
                        e.append(c[z])
                elif c[z]==l[z]:
                        e.append(c[z])
        z+=1
                
        print(e)
minimum_value_array_list()
        
