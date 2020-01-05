def degree_calc():
        import math
        l=[]
        c=[]
        for i in range(5):      
                x=int(input("Enter the values : "))        
                y=(5/9)*(x-32)
                y=round(y)
                l.insert(i,x)          
                c.insert(i,y)
                i+=1        
        print("degree in farenhiet is {} ".format(l))
        print("degree in celcius is {} ".format(c))

        
degree_calc()
