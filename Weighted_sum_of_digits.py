def Weighted_sum_of_digits():
        l=[]
        c=[]
        x=int(input("Enter the values : "))
        for i in str(x)[::-1]:
                j=0
                l.insert(j,int(i))
        
        k=int(len(l))
        for h in range(0,k):
                f=l[h]*(h+1)
                c.insert(h,f)
        d=sum(c)
        print("The Weighted sum of {} is {}.".format(x,d))
                

                
Weighted_sum_of_digits()
