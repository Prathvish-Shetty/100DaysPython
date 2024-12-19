import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

# my_label.pack(expand=True)
# my_label.pack(side="left")

# packer is one of Tks geometry management mechanisms

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    # print("I got clicked")
    # my_label["text"] = "Button got clicked"
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="new button")
new_button.grid(column=2, row=0)

input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
print(input.get())

window.mainloop()

# we cant mix up grid and pack in same program
