#de knoppen/ inputs van de applicatie/ control eenheden
import settings
import Model
import View
import tkinter as tk

from tkinter import *
from tkinter import ttk


def init():
    style = ttk.Style() # voor de widget styles
    settings.root.title("Test in MVC")
    settings.rightframe.pack_propagate(0)
    settings.arduinoframe.pack_propagate(0)
    settings.afstandcensorframe.pack_propagate(0)
    settings.lichtcensorframe.pack_propagate(0)
    settings.temperatuurcensorframe.pack_propagate(0)
    settings.leftframe.pack_propagate(0)
    settings.menu.add_command(label="refresh", command=lambda: refresh(settings.com_list[0], settings.com_list[0].info))
    settings.menu.add_command(label="grafieken", command=lambda: grafieken())
    #.menu.add_command(label="225", command=lambda: get_shit(settings.com_list[0], settings.com_list[0].info))

def grafieken():
    print("loading graphs")
    View.plt.show()


def clearright():
    list = settings.rightframe.pack_slaves()
    for i in list:
        i.destroy()

def get_shit(device, info):
    device.get_temp_licht(info)

def clearall():
    list = settings.rightframe.pack_slaves()
    for i in list:
        i.destroy()
    list2 = settings.arduinoframe.pack_slaves()
    for i in list2:
        i.destroy()
    list3 = settings.afstandcensorframe.pack_slaves()
    for i in list3:
        i.destroy()
    list4 = settings.lichtcensorframe.pack_slaves()
    for i in list4:
        i.destroy()
    list5 = settings.temperatuurcensorframe.pack_slaves()
    for i in list5:
        i.destroy()

def get_data(device, info):
    data = device.get_light(info)
    print(data)
    settings.licht.set(data)

def refresh(device, info):
    #settings.com_list = []
    #print(device)
    #device.destroy()
    #print(device)
    #Model.init()
    #print(device)
    device.checksensors(info)
    startscreen()


def startscreen():
    clearall()
    if len(settings.com_list) == '0':
        tk.Label(settings.leftframe, text="Geen censoren aangesloten", bg='white').pack()
    if settings.arduinoconnected == '1':
        tk.Button(settings.arduinoframe, text=str(settings.name),command=lambda: arduinosettingbuttons(settings.com_list[0], settings.com_list[0].info),height=35, width=35, bg="white").pack()
    else:
        tk.Label(settings.arduinoframe, text='arduino not connected', bg='white').pack()
    if settings.afstandconnected == '1':
        tk.Button(settings.afstandcensorframe, text=str('Afstandscensor'),command=lambda: afstandsettingbuttons(settings.com_list[0], settings.com_list[0].info),height=35, width=35, bg="white").pack()
    else:
        tk.Label(settings.afstandcensorframe, text='afstand not connected', bg='white').pack()
    if settings.tempconnected == '1':
        tk.Button(settings.temperatuurcensorframe, text=str('Temperatuur'),command=lambda: temperatuursettingbuttons(settings.com_list[0], settings.com_list[0].info),height=35, width=35, bg="white").pack()
    else:
        tk.Label(settings.temperatuurcensorframe, text='temperatuur not connected', bg='white').pack()
    if settings.lichtconnected == '1':
        tk.Button(settings.lichtcensorframe, text=str('lichtcensor'),command=lambda: lichtsettingbuttons(settings.com_list[0], settings.com_list[0].info),height=35, width=35, bg="white").pack()
    else:
        tk.Label(settings.lichtcensorframe, text='licht not connected', bg='white').pack()

    settings.root.mainloop()

def arduinosettingbuttons(device, info):
    print(device, info)
    clearright()

    tk.Label(settings.rightframe, text="Options", bg="white").pack()
    tk.Radiobutton(settings.rightframe, text='manual', value = '0', variable = settings.option, bg="white").pack(anchor=W)
    tk.Radiobutton(settings.rightframe, text='temperatuur', value = '1', variable = settings.option, bg="white").pack(anchor=W)
    tk.Radiobutton(settings.rightframe, text='licht', value = '2', variable = settings.option, bg="white").pack(anchor=W)
    tk.Radiobutton(settings.rightframe, text='temp of licht', value = '3', variable = settings.option, bg="white").pack(anchor=W)
    tk.Radiobutton(settings.rightframe, text='Tenp en licht', value = '4', variable = settings.option, bg="white").pack(anchor=W)
    tk.Button(settings.rightframe, text='Apply', command=lambda: device.change_type_write(settings.com_list[0].info), bg="white", width=150).pack()
    tk.Button(settings.rightframe, text='Get Data', command=lambda: device.get_data_type(settings.com_list[0].info), bg="white", width=150).pack()


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()

def afstandsettingbuttons(device, info):
    print(device, info)
    clearright()

    tk.Label(settings.rightframe, text="Options", bg="white").pack()
    label2 = tk.Label(settings.rightframe, text="Max Distance", bg="white").pack()
    entry2 = tk.Entry(settings.rightframe, textvariable=settings.max_distance, bg="white", width=5).pack()
    button2 = tk.Button(settings.rightframe, command=lambda: device.set_max_distance(settings.com_list[0].info), text='Apply max', bg="white", width=10).pack()
    label1 = tk.Label(settings.rightframe, text="Min Distance", bg="white").pack()
    entry1 = tk.Entry(settings.rightframe, textvariable = settings.min_distance, bg="white", width=5).pack()
    button1 = tk.Button(settings.rightframe, command = lambda: device.set_min_distance(settings.com_list[0].info), text='Apply min', bg="white",width=10).pack()


def lichtsettingbuttons(device, info):
    print(device, info)
    clearright()

    tk.Label(settings.rightframe, text="Options", bg="white").pack()
    label1 = tk.Label(settings.rightframe, text="Toggle light", bg="white").pack()
    entry1 = tk.Entry(settings.rightframe, textvariable=settings.toggle_light, bg="white", width=5).pack()
    button1 = tk.Button(settings.rightframe, command=lambda: device.set_toggle_light(settings.com_list[0].info),
                        text='Apply', bg="white", width=5).pack()

def temperatuursettingbuttons(device, info):
    print(device, info)
    clearright()

    tk.Label(settings.rightframe, text="Options", bg="white").pack()
    label1 = tk.Label(settings.rightframe, text="Toggle temperature", bg="white").pack()
    entry1 = tk.Entry(settings.rightframe, textvariable=settings.toggle_temp, bg="white", width=5).pack()
    button1 = tk.Button(settings.rightframe, command=lambda: device.set_toggle_temp(settings.com_list[0].info),
                        text='Apply', bg="white", width=5).pack()

    settings.root.mainloop()


