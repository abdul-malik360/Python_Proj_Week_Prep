from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Welcome Mr G")


Label(root, text="Welcome Mr G!!!").place(x=50, y=30)

mr_gpic = PhotoImage(file = "Mr G pic.PNG")

# place image
background = Label(root, image=mr_gpic,).place(x=0, y=50)

def next():
    root.destroy()
    import age

next_btn = Button(root, text="Next Screen", command=next)
next_btn.place(x=50, y=400)

root.mainloop()