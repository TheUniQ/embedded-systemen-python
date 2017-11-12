#file for global variables
from tkinter import *
import tkinter as tk
from tkinter import ttk

global com_list
com_list = []

global root
root = Tk()

global option
option = StringVar()

global arduinoconnected
arduinoconnected = ""

global name
name = "Arduino"

global lichtconnected
lichtconnected = ""

global tempconnected
tempconnected = ""

global afstandconnected
afstandconnected = ""

root.resizable(width=False, height=False)

global leftframe
leftframe = tk.Frame(root, width=200, height=200, bg="white")
leftframe.pack(side=LEFT, fill=BOTH)

global arduinoframe
arduinoframe = tk.Frame(leftframe, width=200, height=50, bg="white")
arduinoframe.pack(fill=BOTH)

global afstandcensorframe
afstandcensorframe = tk.Frame(leftframe, width=200, height=50, bg="white")
afstandcensorframe.pack(fill=BOTH)

global lichtcensorframe
lichtcensorframe = tk.Frame(leftframe, width=200, height=50, bg="white")
lichtcensorframe.pack(fill=BOTH)

global temperatuurcensorframe
temperatuurcensorframe = tk.Frame(leftframe, width=200, height=50, bg="white")
temperatuurcensorframe.pack(fill=BOTH)

global rightframe
rightframe = tk.Frame(root, width=200, height=200, bg="white")
rightframe.pack(side=LEFT, fill=BOTH)

global Menu
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)

global licht
licht = StringVar()

global temp
temp = StringVar()

global min_distance
min_distance = IntVar()

global max_distance
max_distance = IntVar()