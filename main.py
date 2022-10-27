import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# to add padding
window.config(padx=100, pady=100)

# label

my_label = tkinter.Label(text="I am a label", font=("Arial", 20))
my_label.grid(column=0, row=0)
# add padding
my_label.config(padx=100,pady=100)


# Button

def button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Button 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=30)
input.grid(column=3, row=3)




window.mainloop()
