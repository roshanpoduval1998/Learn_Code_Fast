# class with attributes and methods

class Cat():

    def __init__(self,breed,name,spots):

        self.breed = breed
        self.name = name
        self.spots = spots

    # operation/argument and not a funtion here
    # Is only called by class attributes later
    # Is basically called as Method for Class 
    def meow(self,ID):# Here ID doesn't need to be called as self.ID as its explicitly defined
        
        # .format(self.name,self.breed)) is used by the method to access the __int__ fuction
        print("I will sound meow, by the way my name is {} and I'm {} type of cats breed".format(self.name,self.breed))
        print("& my ID is {}".format(ID))


my_cat = Cat("Tiger", "Tigor", True)

print(my_cat) # prints location of class variable i.e. <__main__.Cat object at 0x000001B0B2BD4A90>

my_cat.meow(3) # method is initialized with the class variable my_cat which is initialized with __init__ of class, Here 3 = ID
#just using "meow(3)" will give error since its not called by the class


