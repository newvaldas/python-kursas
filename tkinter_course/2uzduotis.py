# 2 užduotis

# Patobulinti 1 užduoties programą, kad ji:
# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką,
# bet ir paspaudus mygtuką "Enter"

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
window.bind("<Return>", lambda event: submit())   # <- veikimas su Enter

name.pack()
button.pack()
field.pack()
result.pack()

window.mainloop()