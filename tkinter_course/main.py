# from tkinter import Tk, Label

# window = Tk()
# window.title("Test")
# window.geometry("250x200")
# text = Label(window, text="This is a text")
# text_two = Label(window, text="This is a text2")
# text.pack()
# text_two.pack()
# window.mainloop()

# from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y # <- konstantos

# window = Tk()

# top = Frame(window)
# bottom = Frame(window)

# button1 = Button(top, text="Button #1")
# button2 = Button(top, text="Button #2")
# button3 = Button(top, text="Button #3")
# button4 = Button(top, text="Button #4")

# top.pack()
# bottom.pack(side=BOTTOM)

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT, fill=Y)

# window.mainloop()



# from tkinter import Checkbutton, Entry, Tk, Frame, Button, Label, Entry, Checkbutton, E


# window = Tk()
# window.geometry("250x200")

# text1 = Label(window, text="Name")
# field1 = Entry(window)
# text2 = Label(window, text="Surname")
# field2 = Entry(window)
# check_button = Checkbutton(window, text="Mark me please")

# text1.grid(row=0, column=0, sticky=E)
# field1.grid(row=0, column=1)
# text2.grid(row=1, column=0, sticky=E)
# field2.grid(row=1, column=1)
# check_button.grid(row=2, columnspan=4)


# window.mainloop()


# from tkinter import Tk, Button

# window = Tk()
# window.geometry("250x200")

# def say_hello():
#     print("Hello")

# button1 = Button(window, text="Say Hi", command=say_hello)
# button1.pack()
# window.mainloop()


# from tkinter import Tk, Button

# window = Tk()
# window.title("Push the button")
# window.geometry("150x100")

# def print1(event):
#     print("You pressed left mouse button")

# def print2(event):
#     print("You pressed right mouse button")

# def print3(event):
#     print("You pressed ENTER button")

# button = Button(window, text="Press me", height=10, width=10)
# button.bind("<Button-1>", print1)  #https://web.archive.org/web/20190515021108id_/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html
# button.bind("<Button-2>", print2)
# window.bind("<Return>", print3)

# button.pack()
# window.mainloop()

# from tkinter import Tk, Button
# window = Tk()
# window.geometry("300x200")

# def print1():
#     print("I am printing!")

# button = Button(window, text="Press me to print!", command=print1)
# window.bind("<Return>", lambda event: print1())
# button.pack()

# window.mainloop()

#Kaip per grafinę sąsają ivesti ir atspausdinti duomenis:


# from tkinter import *

# window = Tk()

# def print1():
#     input1 = field1.get()  #  
#     print(input1) 
#     result["text"] = input1

# # tkinter objektai

# text1 = Label(window, text="Enter a word")
# field1 = Entry(window)
# button  = Button(window, text="Enter", command=print1)
# result = Label(window, text="")

# # lenteles stilius
# text1.grid(row=0, column=0)
# field1.grid(row=0, column=1)
# button.grid(row=0, column=2)
# result.grid(row=1, columnspan=3)

# window.mainloop()


# Kaip pridėti sąrašo slinkimo juostą:

# from tkinter import *
# window = Tk()
# window.geometry("350x250")
# list = range(1, 200)
# scrollbar = Scrollbar(window)
# box = Listbox(window, width=20, height=50)

# scrollbar.config(command=box.yview)
# box.insert(END, *list)
# scrollbar.pack(side=RIGHT, fill=Y)
# box.pack(side=LEFT)
# window.mainloop()


# Kaip pasiimti duomenis iš pažymėtos sąrašo vietos:

# from tkinter import *

# langas = Tk()
# sarasas = range(1, 200)

# def spausdinti():
#     pasirinkta = sarasas[boksas.curselection()[0]]  # curseselcetion grazina indexa is listo
#     uzrasas["text"] = pasirinkta

# mygtukas = Button(langas, text="Spausdinti",
# command=spausdinti)

# uzrasas = Label(langas, text="Nieko")
# boksas = Listbox(langas, selectmode=SINGLE)
# boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)
# mygtukas.pack()
# uzrasas.pack()
# langas.mainloop()

#Kaip sukurti meniu:

# from tkinter import *
# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()

#Kaip meniu punktams priskirti funkcijas:

# from tkinter import *
# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)

# def antras():
#     print("Antras!")

# def pirmas():
#     print("Pirmas!")

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras",
# command=antras)
# langas.mainloop()

# Antras!

#Kaip sukurti daugiau meniu, juos atskirti:

# from tkinter import *
# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
# submeniu2 = Menu(meniu, tearoff = 0)
# submeniu3 = Menu(meniu, tearoff = 0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")

# submeniu.add_command(label="Antras")
# submeniu.add_separator()
# submeniu.add_command(label="Trečias")

# meniu.add_cascade(label="Meniu 2",
# menu=submeniu2)
# submeniu2.add_command(label="1")
# submeniu2.add_command(label="2")

# meniu.add_cascade(label="Meniu 3",
# menu=submeniu3)

# langas.mainloop()


# Kaip per grafinę sąsają nuskaityti ir atspausdinti duomenis:

# from tkinter import *

# langas = Tk()

# def spausdinti():
#     ivesta = laukas1.get()
#     rezultatas["text"] = ivesta

# uzrasas1 = Label(langas, text="Įrašykite žodį")
# laukas1 = Entry(langas)
# mygtukas = Button(langas, text="Įvesti", command=spausdinti)
# rezultatas = Label(langas, text="")

# uzrasas1.grid(row=0, column=0)
# laukas1.grid(row=0, column=1)
# mygtukas.grid(row=0, column=2)
# rezultatas.grid(row=1, columnspan=3)

# langas.mainloop()

# Statuso juostos (status bar) kūrimas:

# from tkinter import *
# langas = Tk()
# langas.geometry("300x200")

# def daryti():
#     status["text"] = "dabar daro"


# mygtukas = Button(langas, text="Daryti", command=daryti)
# status = Label(langas, text="Nieko nedaro...", bd=8, relief=RAISED)
# status.pack(side=BOTTOM, fill=X)

# mygtukas.pack()

# langas.mainloop()


#Kaip sukurti veikiančią nuorodą:


# from tkinter import *    
# import webbrowser

# def callback(url):
#     webbrowser.open_new(url)

# root = Tk()
# link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

# link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
# link2.pack()
# link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

# root.mainloop()

# Kaip atidaryti nuotrauką:

# from tkinter import *
# from PIL import ImageTk, Image
# import os

# root = Tk()
# img = ImageTk.PhotoImage(Image.open("paveiksliukas.jpg"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop()

# Kintamųjų naudojimas Tkinter programoje:

#  from tkinter import *

# langas = Tk()

# def spausdinti():
#     ivesta = laukas1.get()
#     rezultatas["text"] = ivesta

# uzrasas1 = Label(langas, text="Įrašykite žodį")
# laukas1 = Entry(langas)
# mygtukas = Button(langas, text="Įvesti", command=spausdinti)
# rezultatas = Label(langas, text="")

# uzrasas1.grid(row=0, column=0)
# laukas1.grid(row=0, column=1)
# mygtukas.grid(row=0, column=2)
# rezultatas.grid(row=1, columnspan=3)

# langas.mainloop()

# Kaip tkinter programoje padaryti kelis langus:

import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()