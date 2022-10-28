# Simple Addition Project : Aman Kumar Mukhi

from tkinter import *

root = Tk()
root.title("Addition Operation")


title_label=Label(root,text="Find out the additon operaton between two natural numbers :").grid(row=0,column=0,columnspan=2)

def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    sum = n1+n2
    e3.insert(0,sum)

    done = Label(root,text="Done",fg="green")
    done.grid(row=6,column=0)

def clr():
    e1.delete(0, END)
    e2.delete(0, END)
    
def clr_all():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

    done = Label(root,text="        ")
    done.grid(row=6,column=0)

# Entry Fields

e1=Entry(root,width=45,borderwidth=5)
e1.grid(row=1,column=1,columnspan=2)

e2=Entry(root,width=45,borderwidth=5)
e2.grid(row=2,column=1,columnspan=2)

e3=Entry(root,width=50,borderwidth=5)
e3.grid(row=4,column=1,columnspan=2)


# Define Labels

first_label=Label(root,text="First no. = ")
first_label.grid(row=1,column=0)

second_label=Label(root,text="Second no. = ")
second_label.grid(row=2,column=0)

result_label=Label(root,text="Result = ")
result_label.grid(row=4,column=0)




# Define Button

result_button = Button(root,text="ADD",padx=15,pady=5,command=add)
result_button.grid(row=3,column=1)

clear_button = Button(root,text="Clear",padx=15,pady=5,command=clr)
clear_button.grid(row=3,column=2)

clear_button = Button(root,text="Clear ALL",padx=15,pady=5,command=clr_all)
clear_button.grid(row=5,column=1)


root.mainloop()
