def even_odd():
        l=[]
        c=[]
        x=int(input("Enter the starting range value :"))
        y=int(input("Enter the Ending range value :"))
        if x<y:
                for i in range(x,y,2):
                        l.append(i)
                        i+=1
                print("Even number from 1 to 100 : {}".format(l))
                for j in range(x+1,y+1,2):
                        c.append(j)
                        j+=1
                print("odd number from 1 to 100 : {}".format(c))
        else:
                print("OOPS! Staring range cannot be greater than ending range")
        
even_odd()                
