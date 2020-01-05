def tuple_form():
        l=[]
        x=int(input("Enter the range: "))
        for i in range(0,x):
                c=input("enter the value: ")
                l.insert(i,c)
                i+=1
        print(l)
        r=tuple(l)
        print(r)
tuple_form()
