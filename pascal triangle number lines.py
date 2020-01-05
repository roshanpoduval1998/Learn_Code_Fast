x = int(input("Enter the number"))
num = 1
for i in range(0,x):
        for j in range(i+1):
                print(num, end = " ")
        num+=1
        print("\n")
num = 1
for i in range(0,x):
        for j in range(i+1):
                print(num**2, end = " ")
        num+=1
        print("\n")
num = 1         
for i in range(0,x):
        for j in range(i+1):
                print(num**3, end = " ")
        num+=1
        print("\n")
