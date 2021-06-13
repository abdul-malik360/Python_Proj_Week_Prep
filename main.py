from tkinter import *
from tkinter import messagebox
from playsound import playsound
root = Tk()
root.geometry("500x500")
root.title("Login Details")

user_name = StringVar()
password = StringVar()

Label(root, text="Enter Details: ").place(x=150, y=50)

Label(root, text="Username: ").place(x=20, y=90)

name_ent = Entry(root, text=" ", width=25, textvariable=user_name)
name_ent.focus()
name_ent.place(x=120, y=90)

Label(root, text="Password: ").place(x=20, y= 130)
password_ent = Entry(root, text=" ", width=25, textvariable=password, show="*")
password_ent.place(x=120, y=130)


def access():
    user_names = ["Mr G"]
    passwords = ["0000"]

    n = len(user_names)
    p = len(passwords)
    found = False

    for x in range(n):

        if name_ent.get() == user_names[x] and password_ent.get() == passwords[x]:
            found = True

    if found == True:
        playsound("granted.mp3")
        messagebox.showinfo("Login Successful", "Access Granted!")
        root.destroy()

        if user_names[x] == "Mr G":
            import mr_g


    else:
        playsound("error.mp3")
        messagebox.showinfo("Login Failed", "Access Denied!")


def clear():
    name_ent.delete(0, END)
    password_ent.delete(0, END)


def close_program():
    root.destroy()


login = Button(root, text="Login", borderwidth="5", command=access)
login.place(x=260, y=170)

clear_btn = Button(root, text="Clear", borderwidth="5", command=clear)
clear_btn.place(x=120, y=270)

close = Button(root, text="close", borderwidth="5", command=close_program)
close.place(x=260, y=270)


root.mainloop()
