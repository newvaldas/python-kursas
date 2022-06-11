# 3 užduotis

# Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu",
#kuriame:

#-> Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje,
# kurioje spausdinamas pasisveikinimo tekstas
#-> Būtų punktas "Atkurti", 
# kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
#-> Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
#-> Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys

from tkinter import *

def submit():
    user_input.set(field.get())
    print(user_input)
    result["text"] = f"Hello, {user_input.get()}"

def delete():       # delete funkcija
    result["text"] = ""
    field.delete(0, 500)

def restore():
    result["text"] = f"Hello, {user_input.get()}"
    

window = Tk()
user_input = StringVar() # atlieka restore funkcija

#menu pridejimas
meniu = Menu(window)            
window.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Delete", command=delete)
submeniu.add_command(label="Restore", command=restore) # restore mygtukas
submeniu.add_separator()  # bruksnio pridejimas
submeniu.add_command(label="Exit", command=window.destroy)


window.geometry("300x100")

name = Label(window, text="Enter your name")
button = Button(window, text= "Enter", command=submit)
field = Entry(window)
result = Label(window, text="")
window.bind("<Return>", lambda event: submit())   # <- veikimas su Enter

name.pack()
button.pack()
field.pack()
result.pack()

window.mainloop()