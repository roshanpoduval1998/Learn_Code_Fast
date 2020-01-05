#-**Kwarg definition
def multiply(**kwargs):
    i = 1
    k = 0
    j = 1
    h = 0
    x = str(input("Which value do you want?"))
    if x == 'value1':
        for num in kwargs['value1']:
            i = i * num
            k+=1
        print("The consisitng multiplicator for value1 is {} : ".format(i))
    elif x == 'value2':
        for num in kwargs['value2']:
            j = j * num
            h+=1
        print("The consisitng multiplicator for value2 is {} : ".format(j))

#-Kwarg dictionary creation
j = 0
print("Enter the 4 values")
list1 = []
for i in range(4):
    x = int(input("::"))
    list1.insert(j,x)
    j+=1
print("Enter the 4 princple")
list2 = []
for i in range(4):
    x = int(input("::"))
    list2.insert(j,x)
    j+=1

multiply(value1 = tuple(list1), value2 = tuple(list2))

    

