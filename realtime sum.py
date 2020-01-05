def realtime_sum():
        n=input("number of inputs : ")
        #n is number of element in list
        l=[]
        #initializing 0 values in list
        for i in range(int(n)):
                x=int(input("enter the values"))
                #number must be int hent put int before input
                l.insert(i,x)
                #enters value i till range of n using x
                i=i+1
                #increment i by 1  
        print(l)
        #print new updated list 
        Sum=sum(l)
        #sum of all elements in the list
        print(Sum)
        
realtime_sum()
