# 1 užduotis

# Sukurti programą su grafine sąsaja, kuri:

# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"

from tkinter import *


def submit():
    user_input = field.get()
    print(user_input)
    result["text"] = (f"Hello, {user_input} ")
     
    

window = Tk()
window.geometry("300x100")

name = Label(window, text="Enter your name")
button = Button(window, text= "Enter", command=submit)
field = Entry(window)
result = Label(window, text="")


name.pack()
button.pack()
field.pack()
result.pack()

window.mainloop()

