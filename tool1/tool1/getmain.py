from main import *
from tkinter import *

import tkinter.messagebox

to=tkinter.Tk()

use1=""
use2=""


def retrieve_input():
	to.configure(background="red")
	global use1 
	use1 = e1.get("1.0","end-1c")
	global use2 
	use2 = e2.get("1.0","end-1c")
	print(use1)
	print(use2)
	fun1(use1,use2)
	




l1=Label(to,text="name")

l1.place(x=1,y=1)
l2=Label(to,text="website address")

l2.place(x=1,y=90)
e1=Text(to,height=3,width=20)

e1.place(x=1,y=20)
e2=Text(to,height=3,width=20)

e2.place(x=1,y=110)



B = tkinter.Button(to, text ="crawl", command =lambda: retrieve_input())


B.place(x=5,y=170)
to.mainloop()
