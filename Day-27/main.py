import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="Hello world", font=("Arial", 24, "normal"))
label.pack()

def button_clicked():
    label.config(text=user_input.get())

user_input = tkinter.Entry()
user_input.pack()

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()