import cx_Freeze
import sys
import os
import json
import random
from tkinter import *
import tkinter as tk
import win32com.client
from tkinter import ttk
from functools import partial
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("PyDiction.pyw", base=base, icon='main_icon.ico')]

cx_Freeze.setup(
    name = "PyDiction",
    options = {"build_exe":{"packages":["tkinter","json","win32com.client","functools","random"]
              ,"include_files":[(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll')),(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'))
            ,(os.path.join("buttons","histroy.png")),(os.path.join("buttons","random.png")),(os.path.join("buttons","printer.png"))
            ,(os.path.join("buttons","save.png")),(os.path.join("buttons","speak.png")),(os.path.join("buttons","submit.png"))
            ,(os.path.join("icons","main_icon.ico")),(os.path.join("icons","error.ico")),("DATA__.json")]}},
    version = "1.01",
    description = "PyDiction a Dictionary",
    executables = executables
    )
















