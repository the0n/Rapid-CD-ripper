import os.path
import tkinter
from tkinter import *
from tkinter import filedialog, StringVar, IntVar
import os
import subprocess
import sys
from tkinter import ttk

cen=tkinter.Tk()
cen.eval('tk::PlaceWindow . center')
# w=300
# h=100
# ws=info.winfo_screenwidth()
# hs=info.winfo_screenheight()
# x= (ws/2) - (w/2)
# y= (hs/2) - (h/2)
# info.geometry('%dx%d+%d+%d' % (w, h, x, y))
frame = Frame(cen, width=350, height=100, background="white")
cen.title("PROCES KOPIOWANIA")
cen.configure(bg="white")
progbar=ttk.Progressbar(cen, orient=HORIZONTAL, length=220, mode="indeterminate")
progbar.place(x=70, y=50)
progbar.start()

def end():
	#os.system("sudo killall abcde
	can=subprocess.Popen(["sudo", "killall", "abcde"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	#os.system("sudo pkill -f  can.py")
	
	#kill= subprocess.Popen("killall abcde", shell=True, stdout=subprocess.PIPE)
	
	cen.destroy()

bend=Button(cen, text="CANCEL", command=end)
bend.pack(side=TOP)
frame.pack()
cen.mainloop()
