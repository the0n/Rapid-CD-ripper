import os.path
from tkinter import *
from tkinter import filedialog, StringVar, IntVar
import os
import subprocess

pid_name="pid.txt"  
whereis="/home"  
plex=os.path.join(whereis, pid_name)
tstet=open(plex, "rt")
op=tstet.read()
tstet.close()

print(op)

while True:  #Sprawdzenie czy aplikacja cmd_2.py wciąż działa.
    
    if not os.path.exists("/proc/"+op):
        name="abcde.conf"  
        local= "/etc"  
        docel=os.path.join(local, name)
        te=open(docel, "wt")
    
        imie="kopiuj.conf"  
        lokali= "/etc"  
        copy=os.path.join(lokali, imie)
        tcp=open(copy, "rt")
        dit=tcp.read()
    
        te.write(dit)
        print("Plik został nadpisany")
        break
    
print("Ostatni")


