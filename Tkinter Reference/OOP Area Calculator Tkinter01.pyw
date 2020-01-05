from tkinter import *
import tkinter as tk
import math

root = tk.Tk()
root.geometry("300x300")
root.title("Area Calculator")


class Area():

	pi = 3.14

	def __init__(self,base,height,length,breadth,radius):

		self.base = base
		self.height = height
		self.radius = radius
		self.length = length
		self.breadth = breadth
		self.triangle_area = base * height * 0.5
		self.rectangle = length * breadth
		self.cylinder = round(((2 * Area.pi * (radius ** 2)) + (2 * Area.pi * radius * height)),3)
		self.cone = round((Area.pi * radius* (radius + math.sqrt((height*height)+(radius*radius)))),3)
		x = 1

	def triangle():

		try:
			r = Entry1.get()
			s = Entry2.get()
			t = int(r)
			v = int(s)
			my_triangle = Area(t,v,0,0,0)
			z = my_triangle.triangle_area
			label = tk.Label(root, text="Area of Triangle is {}".format(z))
			label.grid(row=6,column=1)
		except:
			label = tk.Label(root, text="Incorrect Input")
			label.grid(row=6,column=1)

	def rectangle():

		try:
			r = Entry1.get()
			s = Entry2.get()
			t = int(r)
			v = int(s)
			my_rectangle = Area(0,0,t,v,0)
			z = my_rectangle.rectangle
			label = tk.Label(root, text="Area of Rectangle is {}".format(z))
			label.grid(row=6,column=1)
		except:
			label = tk.Label(root, text="Incorrect Input")
			label.grid(row=6,column=1)


	def cylinder():

		try:
			r = Entry1.get()
			s = Entry2.get()
			t = int(r)
			v = int(s)
			my_cylinder = Area(0,v,0,0,t)
			z = my_cylinder.cylinder
			label = tk.Label(root, text="Area of cylinder is {}".format(z))
			label.grid(row=6,column=1)
		except:
			label = tk.Label(root, text="Incorrect Input")
			label.grid(row=6,column=1)

	def cone():

		try:
			r = Entry1.get()
			s = Entry2.get()
			t = int(r)
			v = int(s)
			my_cone = Area(0,v,0,0,t)
			z = my_cone.cone
			label = tk.Label(root, text="Area of cone is {}".format(z))
			label.grid(row=6,column=1)
		except:
			label = tk.Label(root, text="Incorrect Input")
			label.grid(row=6,column=1)

	def clear():
		label = tk.Label(root, text="                                           ")
		label.grid(row=6,column=1)
		Entry1.delete(0, END)
		Entry2.delete(0, END)


Entry1 = tk.Entry(root)
Entry1.grid(row=0,column=1)
Entry2 = tk.Entry(root)
Entry2.grid(row=1,column=1)

label = tk.Label(root, text="")
label.grid(row=6,column=1)

button = tk.Button(root, text="Cone",command=Area.cone)
button.grid(row=4,column=2)

button = tk.Button(root, text="Clear",command=Area.clear)
button.grid(row=3,column=2)

button = tk.Button(root, text="Cylinder",command=Area.cylinder)
button.grid(row=5,column=1)

button = tk.Button(root, text="Rectangle",command=Area.rectangle)
button.grid(row=4,column=1)

button = tk.Button(root, text="Triangle",command=Area.triangle)
button.grid(row=3,column=1)


root.mainloop()