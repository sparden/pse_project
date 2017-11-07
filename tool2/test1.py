from test import *
from tkinter import *
import tkinter.messagebox

to = tkinter.Tk()

use1=""
use2=""

def retrieve_input():
	global use1
	use1 = e1.get("1.0","end-1c")
	
	f = open(use1,"r")
	print(f.read())
	record()
	
def stop_recording():
	
	print("stopped!")
	stop()

def save_recording():
	save()
	print("done")

l1=Label(to,text="text")
l1.place(x=90,y=1)
#l2=Label(to,text="website address")
#l2.place(x=1,y=90)
e1=Text(to,height=3,width=20)
e1.place(x=30,y=20)
#e2=Text(to,height=3,width=20)
#e2.place(x=1,y=110)

B = tkinter.Button(to, text ="record", command =lambda: retrieve_input())
B.place(x=5,y=170)

B2 = tkinter.Button(to, text ="stop", command =lambda: stop_recording())
B2.place(x=80,y=170)
B3 = tkinter.Button(to, text ="save", command =lambda: save_recording())
B3.place(x=140,y=170)
to.mainloop()
