import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import time

title = "FrameWork"

class CreateToolTip(object):

    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 45
        y += self.widget.winfo_rooty() + 25
        # creates a toplevel window
        self.tooltip = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tooltip, text=self.text, relief="flat", justify='right', borderwidth=1, font=("SEGOE UI", "8", "normal"))
        label.pack(ipady=1)

    def close(self, event=None):
        if self.tooltip != True:
            self.tooltip.destroy()

class main_frame(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (IntroPage1,IntroPage2,IntroPage3):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(IntroPage1)

    def show_frame(self, navigation): 

        frame = self.frames[navigation]
        frame.tkraise()

class IntroPage1(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        canvas_main = tk.Canvas(self)
        self.canvas_main = canvas_main
        canvas_layer1 = tk.Canvas(self)
        self.canvas_layer1 = canvas_layer1
        exit_ = ttk.Button(self, text="Exit",command=quit)
        exit_.grid(row=0,column=0)
        Next = ttk.Button(self, text="Next",command=lambda:controller.show_frame(IntroPage2))
        Next.grid(row=0, column=1)
        Page1_Label = ttk.Label(self, text="Page1")
        Page1_Label.grid(row=1, column=0)
        CreateToolTip(exit_, f"Exit {title}")
        CreateToolTip(Next, "Go to Page 2")
        CreateToolTip(Page1_Label,"Info")

class IntroPage2(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        back = ttk.Button(self, text="Back",command=lambda:controller.show_frame(IntroPage1))
        back.grid(row=0,column=0)
        Next = ttk.Button(self, text="Next", command=lambda:controller.show_frame(IntroPage3))
        Next.grid(row=0,column=1)
        Page2_Label = tk.Label(self, text="Page2")
        Page2_Label.grid(row=1,column=0)
        CreateToolTip(back, "Go back to Page 1")
        CreateToolTip(Next, "Go to Page 3")
        CreateToolTip(Page2_Label,"Info")

class IntroPage3(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        back = ttk.Button(self, text="Back", command=lambda:controller.show_frame(IntroPage2))
        back.pack(side='left',fill=X)
        Home = ttk.Button(self, text="Home", command=lambda:controller.show_frame(IntroPage1))
        Home.pack(side='left',fill=X) 
        Page3_Label = tk.Label(self, text="Page3")
        Page3_Label.pack(side='bottom',fill=X,anchor=tk.W)
        CreateToolTip(Home, "Go Home")
        CreateToolTip(back, "Go back to Page 2")
        CreateToolTip(Page3_Label,"Info")

app = main_frame()
app.geometry("640x640")
app.title(str(title))
app.wm_state('zoomed')
app.configure(bg="white")
app.mainloop()
