from tkinter import *
import random
from tkinter import messagebox

def generate_password():
    character_string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror(message="Please key in the required inputs")
        return
    password=""
    if length>6 and length<12:
        if repeat == 1:
            password = random.sample(character_string,length)
        else:
            password = random.choices(character_string,k=length)
    else:
        messagebox.showerror(message="Please Enter Length In Given Range")
    
    password=''.join(password)
    
    password_v = StringVar()
    password="        Generated Password: "+str(password)
    
    password_v.set(password)
    
    password_label = Entry(password_gen, bd=0, bg="gray85", textvariable= password_v, state="readonly")
    password_label.place(x=10, y=140, height=50, width=320)
    

password_gen  = Tk()
password_gen.geometry("350x200")
password_gen.title("Random Password Generator")
title_label = Label(password_gen, text="Random Password Generator", font=('Ubuntu Mono',12))
title_label.pack()

range_label1=Label(password_gen,text="Note:    For Better Security, ")
range_label1.place(x=20,y=30)

range_label2=Label(password_gen,text="      Password length should be in range of 6 to 12   :)")
range_label2.place(x=20,y=50)

length_label = Label(password_gen, text="Enter length of password: ")
length_label.place(x=20,y=80)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190,y=80)

repeat_label = Label(password_gen, text="Enter - 1: No repetition | 2: Otherwise: ")
repeat_label.place(x=20,y=120)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=300,y=120)
password_button = Button(password_gen, text="Generate Password", command=generate_password)
password_button.place(x=100,y=160)

password_gen.mainloop()