from tkinter import *
from tkinter import messagebox
from datetime import date, timedelta
from playsound import playsound

root = Tk()
root.geometry("500x500")
root.title("Age Restriction")

age_ans = StringVar()

year_ent = Entry(root)
year_ent.place(x=50, y=100)
month_ent = Entry(root)
month_ent.place(x=50, y=150)
day_ent = Entry(root)
day_ent.place(x=50, y=200)
Label(root, textvariable=age_ans).place(x=50, y=250)


def calculate():
    dob = date(int(year_ent.get()), int(month_ent.get()), int(day_ent.get()))
    age = (date.today() - dob)//timedelta(days=365.245)
    age_ans.set(age)

    if age < 16:
        playsound("error.mp3")
        messagebox.showerror("Access Denied", "Sorry you're too young")
    elif age > 16:
        playsound("granted.mp3")
        messagebox.showinfo("Access Granted", "Welcome")
        root.destroy()
        import numbers

cal_btn = Button(root, text="CALCULATE", command=calculate)
cal_btn.place(x=50, y=350)





root.mainloop()

