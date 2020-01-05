def factorial():
        input_number = input("Enter The Number For Factorial : ")
        x=int(input_number)
        if x==0:
                print("factorial is 1")
        elif x<0:
                print("factorial of negative number not possible")
        else:
                x=x+1
                y=1
                for c in range(1,x):
                        y=y*c
        print(y)
     
factorial()
                
        
