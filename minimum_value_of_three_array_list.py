def minimum_value_array_list():
        l=[]
        c=[]
        h=[]
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
        for f in range(0,x):
                t=int(input("enter the values : "))
                h.insert(f,t)
                f+=1
        print(h)
        e=[]
        for z in range(0,x):
                if l[z]<c[z]<h[z]:
                        e.append(l[z])
                elif c[z]<l[z]<h[z]:
                        e.append(c[z])
                elif h[z]<c[z]<l[z]:
                        e.append(h[z])
                elif h[z]<l[z]<c[z]:
                        e.append(h[z])
                elif l[z]<h[z]<c[z]:
                        e.append(l[z])
                elif c[z]<h[z]<l[z]:
                        e.append(c[z])
                elif c[z]<=l[z]==h[z]:
                        e.append(c[z])
                elif l[z]<=h[z]==c[z]:
                        e.append(l[z])
                elif h[z]<=c[z]==l[z]:
                        e.append(h[z])
                elif c[z]>=l[z]==h[z]:
                        e.append(h[z])
                elif l[z]>=h[z]==c[z]:
                        e.append(c[z])
                elif h[z]>=c[z]==l[z]:
                        e.append(l[z])
                        
        z+=1
                
        print(e)
minimum_value_array_list()
