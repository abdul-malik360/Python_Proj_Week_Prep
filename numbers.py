from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Generate Your Numbers")

numb_ans = StringVar()
numb_ent = StringVar()
mylist = []
mynewlist = []

ent_numb = Entry(root, textvariable=numb_ent)
ent_numb.place(x=50, y=25)
Label(root, textvariable=numb_ans).place(x=50, y=50)


def generate():
    for x in range(1, 11):
        number = random.randint(1, 60)
        mylist.append(number)
        numb_ans.set(mylist)
        if x in range > 11:
            root.terminate()



gen_btn = Button(root, text="Generate", command=generate)
gen_btn.place(x=50, y=100)






root.mainloop()