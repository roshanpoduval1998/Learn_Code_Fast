def median(*number):
    t = len(n)
    y = sorted(n)
    if len(y)%2==1:
        print(y[t//2])
    else:
        print(sum(y[(t//2)-1:(t//2)+1])/2)
    

n = [20,10,34,56,32,54,45,26,3]
median(n)
