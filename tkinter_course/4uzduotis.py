# Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:

# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas Nuspaudus klaviatūros mygtuką "Escape",
#  uždarytų programos langą


from tkinter import Tk, END, StringVar, Menu, Label, Button, Entry, SUNKEN, W, X, BOTTOM

def submit():
    user_input.set(field.get())
    print(user_input)
    result["text"] = f"Hello, {user_input.get()}"
    change()        #statuso juostos iskvietimas
     

def delete():       # delete funkcija
    result["text"] = ""
    field.delete(0, END)
    status["text"] = "Deleted" #Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas

def restore():
    result["text"] = f"Hello, {user_input.get()}"
    status["text"] = "Restored"

def change():
    status["text"] = "Entered" # Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas


window = Tk()
user_input = StringVar() # atlieka restore funkcija

#menu pridejimas
meniu = Menu(window)            
window.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Delete", command=delete)  # delete mygtukas
submeniu.add_command(label="Restore", command=restore) # restore mygtukas
submeniu.add_separator()  # bruksnio pridejimas
submeniu.add_command(label="Exit", command=window.destroy)

status = Label(window, text="", bd=1, relief=SUNKEN, anchor=W) # statuso juosta
status.pack(side=BOTTOM, fill=X)

window.geometry("300x200")

name = Label(window, text="Enter your name")
button = Button(window, text= "Enter", command=submit)
field = Entry(window)
result = Label(window, text="")
window.bind("<Return>", lambda event: submit())     # <- veikimas su Enter (lamda kaip funkcija)
window.bind("<Escape>", lambda event: window.destroy())   # <- veikimas su Escape

name.pack()
button.pack()
field.pack()
result.pack()
status.pack()

window.mainloop()