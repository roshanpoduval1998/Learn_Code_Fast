#-arg definition
def multiply(args):
    i = 1
    k = 0  
    for num in l:
        i = i * num
        k+=1
    print("The consisitng multiplicator value is {} : ".format(i))

#-arg creation    
j = 0
print("Enter the 10 Inputs")
list1 = []
for i in range(10):
    x = int(input("::"))
    list1.insert(j,x)
    j+=1
l = tuple(list1)
multiply(l)

