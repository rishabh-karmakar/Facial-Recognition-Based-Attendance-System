# from PIL import Image, ImageTk
# from tkinter import Tk, BOTH
# from tkinter.ttk import Frame, Label, Style
import os 
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# print(1)
text_to_speech('Authentication Successful!')
text_to_speech('Welcome!')
text_to_speech('Please browse through your options..')
# print(2)
# text_to_speech('Welcome')

def quit(*args):
    root.destroy()

root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)

titl=Label(root,text="Smart College!!", bd=20, bg="black", fg="green", 
	font=('arial', 48),relief=RIDGE).pack(side=TOP, fill=X)
a=Label(root,text="Welcome to the Facial Recognition", bg="black", fg="yellow", 
	font=("arial", 56)).pack()
a=Label(root,text="Attendance System", bg="black", fg="yellow", 
	font=("arial", 56)).pack()

ri = Image.open("register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(root, image=r)
label1.image = r
label1.place(x=180, y=300)

ai = Image.open("attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(root, image=a)
label2.image = a
label2.place(x=980, y=300)

vi = Image.open("verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(root, image=v)
label3.image = v
label3.place(x=600, y=300)

def register():
  os.system('python Add_New.py')

def verify():
	os.system('python Recog.py')

def attendance():
	os.system('python Attendance.py')

r=Button(root, text="Click to register a new student", bd=10, 
	font=('times new roman',12),bg="black",fg= "yellow", height=5).place( x=115, y=570)

r=Button(root, text="Give Attendance", bd=10, 
	font=('times new roman',12),bg="black",fg= "yellow", height=5).place( x=615, y=570)

r=Button(root, text="View Attendance", bd=10, 
	font=('times new roman',12),bg="black",fg= "yellow", height=5).place( x=1020, y=570)
r=Button(root, text="EXIT", bd=10, 
	command=quit, font=('times new roman',12),bg="black",fg= "yellow", height=2, width= 10).place( x=637, y=700)

if __name__ == '__main__':
   root.mainloop()
   