def minimum_value_array_list():
        import statistics
        list_1=[]
        list_2=[]
        list_3=[]
        x=int(input("Enter the range of list: "))
        for i in range(0,x):
                list_1_input=int(input("enter the values : "))
                list_1.insert(i,list_1_input)
                i+=1
        print(list_1)
        for j in range(0,x):
                list_2_input=int(input("enter the values : "))
                list_2.insert(j,list_2_input)
                j+=1
        print(list_2)
        for k in range(0,x):
                list_3_input=int(input("enter the values : "))
                list_3.insert(k,list_3_input)
                k+=1
        print(list_3)
        median_1=int(statistics.median(list_1))
        print(median_1)
        median_2=int(statistics.median(list_2))
        print(median_2)
        median_3=int(statistics.median(list_3))
        print(median_3)        
                
minimum_value_array_list()

