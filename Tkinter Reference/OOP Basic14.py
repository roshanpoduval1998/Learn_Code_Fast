class Account():

    def __init__(self,owner):
    	owner = {"1234":["roshan",600],"0000":["rohan",100],"1111":["shyam",300],"5678":["manoj",200],"4567":["ganga",300]}
    	d = owner.get(pin)
    	self.name = d[0]
    	self.amount = d[1]
    	print("Hi {}!\nYour Account Balance is {}".format(self.name,self.amount))

        
    def deposit(self,deposit):

        (self.amount)+=(deposit)
        print("Deposited amount = {}\nAccount balance = {}".format(deposit,self.amount))

    def withdraw(self,withdraw):

        if self.amount <= withdraw:
            print("Unable to withdraw funds\nFunds unavailable!!")

        elif self.amount > withdraw:
            self.amount -= withdraw
            print("Amount withdrawn = {}\nAccount balance = {}".format(withdraw,self.amount))



pin = str(input("Enter the 4 digit PIN :: "))
try:
	a = Account(pin)
except:
	print("Incorrect PIN")

deposit=int(input("Enter the deposit amount :: "))
withdraw = int(input("enter the withdraw amount :: "))
a.deposit(deposit)
a.withdraw(withdraw)
