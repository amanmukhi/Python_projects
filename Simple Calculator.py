from tkinter import *
root=Tk()
root.title("Simple Calculator")

#Input Field
e = Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=4)

#Functions
def click_button(number):  
    old_number=e.get()
    e.delete(0, END)        
    e.insert(0, str(old_number) + str(number))

def add():
    first_number = e.get()
    global f_num, check
    check="add"
    f_num=first_number
    e.delete(0, END)

def sub():
    first_number = e.get()
    global f_num, check
    check="sub"
    f_num=first_number
    e.delete(0, END)

def mul():
    first_number = e.get()
    global f_num, check
    check="mul"
    f_num=first_number
    e.delete(0, END)

def div():
    first_number = e.get()
    global f_num, check
    check="div"
    f_num=first_number
    e.delete(0, END)

def equal():
    second_number=e.get()
    e.delete(0, END)
    if check=="add": 
        e.insert(0, int(f_num) + int(second_number))
    
    if check=="sub":
        e.insert(0, int(f_num) - int(second_number))
    
    if check=="mul":
        e.insert(0, int(f_num) * int(second_number))
    
    if check=="div":
        e.insert(0, int(f_num) / int(second_number))
    

def clear():
    e.delete(0, END)

def back():
    old_number = e.get()
    new_number = ( int(old_number) / 10)
    e.delete(0, END)
    e.insert(0, int(new_number))

#Define Buttons 

button_1 = Button(root,text="1",padx=35,pady=10,command=lambda: click_button(1))
button_2 = Button(root,text="2",padx=35,pady=10,command=lambda: click_button(2))
button_3 = Button(root,text="3",padx=35,pady=10,command=lambda: click_button(3))
button_4 = Button(root,text="4",padx=35,pady=10,command=lambda: click_button(4))
button_5 = Button(root,text="5",padx=35,pady=10,command=lambda: click_button(5))
button_6 = Button(root,text="6",padx=35,pady=10,command=lambda: click_button(6))
button_7 = Button(root,text="7",padx=35,pady=10,command=lambda: click_button(7))
button_8 = Button(root,text="8",padx=35,pady=10,command=lambda: click_button(8))
button_9 = Button(root,text="9",padx=35,pady=10,command=lambda: click_button(9))
button_0 = Button(root,text="0",padx=35,pady=10,command=lambda: click_button(0))

button_equal = Button(root,text="=",padx=77,pady=10,command=equal)
button_add = Button(root,text="+",padx=23,pady=10,command=add)
button_sub = Button(root,text="-",padx=25,pady=10,command=sub)
button_mul = Button(root,text="x",padx=24,pady=10,command=mul)
button_div = Button(root,text="%",padx=22,pady=10,command=div)

button_clear = Button(root,text="Clear",padx=110,pady=10,command=clear)
button_back = Button(root,text="Back",padx=15,pady=10,command=back)

#Put All Button on the Screen 
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_add.grid(row=5,column=3)
button_sub.grid(row=4,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=2,column=3)

button_clear.grid(row=1,column=0,columnspan=3)
button_back.grid(row=1,column=3)


root.mainloop()