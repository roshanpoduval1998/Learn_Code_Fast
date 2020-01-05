def pascal(n):    
  a=[1]
  for i in range(n):
      a = list.center(40)
      print("row{}".format(i+1),a)
      l=[]
      l.append(a[0])
      for i in range(len(a)-1):
          l.append(a[i]+a[i+1])
      l.append(a[-1])
      a=l
n = int(input("How many lines of pascal value? \n"))      
pascal(n)
