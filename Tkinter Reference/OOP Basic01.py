# Class is a user defined object by the user
# Where as rest are built in object

""" class Sample():
        pass
    my_sample = Sample()
    type(my_sample)        """

# gives output as " __main__.Sample "
# above program is of no use because beacause it has no attributes

#-----------------------------------------------------------------------------------------------------------------------------------

# let's create class with one attributes

class Dog():

    def __init__(self,mybreed):
        
        # "def __init__():" is a constructer for class       
        # Creating Attributes
        # Take in the argument along with self (here, mybreed)
        # Assign it inside the function using self.attribute_name (here, mybreed)
        self.breed = mybreed

my_dog = Dog(mybreed = "Lab") # initializing the class with the variable my_dog

print(my_dog)# will only show the location of the variable my_dog <__main__.Dog object at 0x0000018D13BA4B00>

# "type(my_dog)" =====> will output as "__main__.Dog"

my_dog.breed # will initialize my_dog with the breed = "Lab"...

print(my_dog.breed) # Method 1 : This will print as "Lab" in output, initiliazing with the class is very important before printing the variables

# or

my_first_breed = my_dog.breed # initializing the output of class variable "value" i.e mybreed = "Lab" with new varialble

print(my_first_breed) # Method 2 : Is similar to Method 1

#------------------------------------------------------------------------------------------------------------------------------------

# lets create multiple attributes

class Cat():

    def __init__(self,breed,name,spots):

        self.breed = breed
        self.name = name
        self.spots = spots

my_cat = Cat(breed = "Lion", name = "leo", spots = False) # Here attributes can be string, number or even boolean 
print(my_cat.breed) # print output as "Lion"
print(my_cat.name) # print output as "leo"
print(my_cat.spots) # print output as False (boolean False and not string)

# or

x = str(my_cat.breed)
y = str(my_cat.name) 
z = str(my_cat.spots)
list_my_cat_01 = [x, y, z] # create an animal profile
print(list_my_cat_01) # print the profile as list ======> "['Lion', 'leo', 'False']"

