import os 
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import cv2
from quit import release

def quit(*args):
    root.destroy()

root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)

Top = Frame(root, bd=10, bg="black", relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=50, bd=30)
Form.pack(side=TOP, pady=20)
##################################################################################
def Back():
    Home.destroy()
    # root.deiconify()
def divert():
	os.system('python screen.py')
#################################################################################
lbl_home=Label(Top, text="Authentication Successful!!", bd=20, bg="black", fg="green", 
	font=('arial', 48),relief=SUNKEN).pack(fill=BOTH)
p=Button(Top, text="Click to proceed further to the Attendance record system.", bg="black", fg="green", 
	font=('verdana', 20), command = lambda:[divert(), quit()]).pack(fill=BOTH, expand=1, ipady=250)	#I love this.
btn_back = Button(Top, text='Back', bd=10, command=quit, bg="white").pack(ipady=20, ipadx=100)


#==============================INITIALIATION==================================
if __name__ == '__main__':
	root.mainloop()

