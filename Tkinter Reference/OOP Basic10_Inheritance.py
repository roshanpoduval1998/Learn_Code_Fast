# Inheritance Example by Roshan Poduval
# Do not import any library while using the function "eval"

class Operators():

    def __init__(self):
        print("The Operation has begun")
        
    def Def_operator(self,x):
        self.add = x.split("+")
        self.sub = x.split("-")
        self.multi = x.split("*")
        self.div = x.split("/")
        
class Operator_evaluator(Operators):

    def __init__(self,x):
        Operators.__init__(self)
        Operators.Def_operator(self,x)
        
        self.x = x

    def evaluate(self):
        try:
            if len(self.add) > 1:
                print("The operator has Addition operator")
            if len(self.sub) > 1:
                print("The operator has Subtraction operator")
            if len(self.multi) > 1:
                print("The operator has Multiplication operator")
            if len(self.div) > 1:
                print("The operator has Division operator")      
            alebraic_expression = eval(self.x)
            return "Answer = {}".format(alebraic_expression)
        except:
            return "Error in the entered string {}.".format(self.x)

x = input("Enter the string :: ")
def my_driver(x):
    a = Operator_evaluator(x).evaluate()
    print(a)
my_driver(x)

y = input("Do you want to quit?\nEnter y/n\t")
if y == "y":
    print("The process has been quit")
    quit()
while y == "n":
    x = input("Enter the string or quit by entering q:: ")
    if x == "q":
        quit()
    else:
        my_driver(x)
