import tkinter as tk
from tkinter import messagebox
import os

class Alphabets():

    def __init__(self):
        pass
    def small_alphabets_generator(self):
        import random
        alphabets = "abcdefghijklmnopqrstuvw"
        alphalist = list(alphabets)
        d = []
        for i in range(2):
            d.append(random.choice(alphalist))
        f = "".join(d)
        return f

    def large_alphabets_generator(self):
    	import random
    	symbol = "ABCDEFGHIJKLMNOPQRSTUVW"
    	f = random.choice(symbol)
    	return f

class Numbers():

    def __init__(self):
        pass
    def numbers_generator(self):
        import random
        number = "1234567890"
        numlist = list(number)
        d = []
        for i in range(4):
            d.append(random.choice(numlist))
        f = "".join(d)
        return f

class Symbols():

    def __init__(self):
        pass

    def symbols_generator(self):
        import random
        symbol = "!@#$%&"
        symlist = list(symbol)
        d = []
        for i in range(1):
            d.append(random.choice(symlist))
        f = "".join(d)
        return f

class Password(Alphabets, Numbers, Symbols):

    def __init__(self):
    	self.a1 = Alphabets.large_alphabets_generator(self)
    	self.a = Alphabets.small_alphabets_generator(self)
    	self.b = Numbers.numbers_generator(self)
    	self.c = Symbols.symbols_generator(self)
    	self.d = self.a+self.b+self.c

    def password(self):
    	import random
    	f = list(self.d)
    	random.shuffle(f)
    	f = "".join(f)
    	d = self.a1 + f
    	return "The OTP is {}".format(d)

root = tk.Tk()
root.geometry("145x95")
root.title("OTP Generator")
root.configure(bg="gray35")

def OTP_Button():
	entry = tk.Entry(root)
	entry.place(x=10,y=30)
	a = Password()
	OTP = a.password()
	print(OTP)
	messagebox.showinfo("OTP", "{}".format(OTP))
	def Verification():
		x = entry.get()
		d = x.split("The OTP is ")
		if str(x) == d[0]:
			os.startfile("F:\\OOP")
			root.destroy()
		elif str(x) != d[0]:
			print("Error")
	button = tk.Button(root, text="Enter", width="10", bg="black", fg="White", command=Verification)
	button.place(x=30,y=50)


button = tk.Button(root, text="Generate OTP", width="10", bg="black", fg="White", command=OTP_Button)
button.place(x=30,y=0)

root.mainloop()
