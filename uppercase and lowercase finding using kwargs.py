#-**Kwarg definition
def upper_lower(*args):
    for string in args[0]:
        c = 0
        i = 0
        if (string.isupper()==True):
            c+=1
        elif (string.islower()==True):
            i+=1
        print(" lower is {} Capital is {}".format(i,c))
#-Kwarg dictionary creation
x = str(input("::"))

upper_lower(x)

    

