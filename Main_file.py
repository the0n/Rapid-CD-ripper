
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import filedialog, StringVar, IntVar
import os
import subprocess
from subprocess import Popen
from PIL import  ImageTk, Image
from  subprocess import check_output, PIPE, Popen
import os.path

import sys
import time
import atexit
import sys
import fcntl


try:
    root=tkinter.Tk()
    frame = Frame(root, width=900, height=600)
    frame.pack()
except:
        messagebox.showinfo("Blad","ZAKONCZENIE PROGRAMU")
root.title("RIPPER")
cdpara=StringVar()
title=StringVar()


cdlist=Label(root,textvariable=cdpara,font=("Arial", 10, 'bold'), justify=LEFT)
cdlist.place(x=300, y=180)

titel=Label(root,textvariable=title,font=("Arial", 10, 'bold'))
titel.place(x=300, y=140)

os.system("sudo apt-get install python3-pil python3-pil.imagetk")

dis=subprocess.Popen("sudo which cd-discid", shell=True, stdout=subprocess.PIPE)
dis_wyn=dis.stdout.read()
dis_str=str(dis_wyn)

subzero=subprocess.Popen("sudo which abcde", shell=True, stdout=subprocess.PIPE)
wynik=subzero.stdout.read()
out=str(wynik)

flamand=subprocess.Popen("sudo which flac", shell=True, stdout=subprocess.PIPE)
flac_first=flamand.stdout.read()
flac_wynik=str(flac_first)

lame=subprocess.Popen("sudo which lame", shell=True, stdout=subprocess.PIPE)

out_lame=lame.stdout.read()
outl=str(out_lame)
print(out)
os.system("sudo apt-get install -y eyed3")  # Instalacja eyed3
if len(out)<5: #Abcde nie zostal wykryty
    os.system(" sudo apt-get install abcde")
    
if len(flac_wynik)<5: #Flac nie zostal wykryty
    os.system(" sudo apt-get install flac")

if len(outl)<5: #Lame nie zostal wykryty
    os.system("sudo apt-get install -y lame")
if len(dis_str)<5: #Discid nie zostal wykryty
    os.system("sudo apt-get install -y cd-discid")

img=(Image.open("Raspberry.png"))
    
def discid():
    try:
        cd_test_sr0= Popen(['sudo', 'blockdev', '--getsize64', '/dev/sr0'],  stdout=subprocess.PIPE) #Sprawdzenie czy cd rom mounted
        # cd_test_sr1= Popen(['sudo', 'blockdev', '--getsize64', '/dev/sr1'],  stdout=subprocess.PIPE) #Test w przypadku innej nazwy cd-rom
    
        cd_pgr_sr0=cd_test_sr0.stdout.read()
        # cd_pgr_sr1=cd_test_sr1.stdout.read()
        rez_id_sr0=str(cd_pgr_sr0)
        # rez_id_sr1=str(cd_pgr_sr1)
        if len(rez_id_sr0)>5:
            runa= Popen(["abcde", "-N"],  stdout=subprocess.PIPE) 
            time.sleep(25)
            killa= Popen(("pkill -9 abcde"),shell=True,  stdout=subprocess.PIPE) 
        elif len(rez_id_sr0)<4:
            messagebox.showinfo("Koniec", "Bład napedu optycznego")
        checkid= Popen(["cd-discid"],  stdout=subprocess.PIPE) 
            
            
        check_out=checkid.stdout.read()
        podek=check_out.decode("utf-8")


        cut=podek[0:8]


        pat=os.getenv('HOME')
        where_file=os.path.join(pat, cut)# W /home/pi/"disc-id"-tutaj lista 
        
        fin=open(where_file, "r")
        li=fin.readlines()
        
        
        if os.path.exists(where_file):
            local= pat
            scie=os.path.join(pat, cut)
            teid=open(scie, "r")
            text="TTITLE"
            haslo="DTITLE"
            lines=teid.readlines()

            new_list=[]

            idx=0
            
            for slowo in lines:
                
                if haslo in slowo:
                    
                    hook=slowo
            readysl=hook.replace("DTITLE", "TYTUL")
            title.set(readysl)
            print(type(hook))

            for line in lines:
                
                if text in line:
                    new_list.insert(idx, line)
                    idx+=1
                    
            te.close()	

            if len(new_list)==0:
                print("NO TEXT")
            else:
                linelen=len(new_list)
                for i in range(linelen):
                    print(end=new_list[i])
            
            strlist=' '.join(new_list)
            next_str=strlist.replace("TTITLE", " ")
            ready_str=next_str.replace("=","  ")
            print(ready_str)
            
            
        else:
            messagebox.showinfo("Koniec", "Brak danych w bazie CDDB")
        cdpara.set(ready_str)
    except:
        messagebox.showinfo("Blad","BLAD SPROBUJ PONOWNIE")
   
def kopiuj_oryg():  #Kopiowanie oryginalnego pliku do folderu-Zapas--ZApas zawiera format podstawowy ogg.
    
    name="abcde.conf"  
    local= "/etc"  
    docel=os.path.join(local, name)
    te=open(docel, "r")
    o2=te.read()
    
    os.system(" cd /etc/; sudo touch kopiuj.conf; sudo chmod -R ugo+rw /etc/kopiuj.conf")
    
    imie="kopiuj.conf"  
    lokali= "/etc"  
    copy=os.path.join(lokali, imie)
    tcp=open(copy, "wt")
    
    
    tcp.write(o2)
    
    
kopiuj_oryg()

def destroy():  #Podmienia na zapas, czyli najpierwszy plik conf.
    

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
    root.destroy()
    sys.exit()


load_cddb=Button(root, text="POBIERZ TYTUŁY Z BAZY", command=discid, background="white")
load_cddb.place(x=62, y=380)
def load():
    try:
        cd_test_sr0= Popen(['sudo', 'blockdev', '--getsize64', '/dev/sr0'],  stdout=subprocess.PIPE) #Sprawdzenie czy cd rom mounted
        #cd_test_sr1= Popen(['sudo', 'blockdev', '--getsize64', '/dev/sr1'],  stdout=subprocess.PIPE) #Test w przypadku innej nazwy cd-rom
    
        cd_pgr_sr0=cd_test_sr0.stdout.read()
        #cd_pgr_sr1=cd_test_sr1.stdout.read()
        rez_id_sr0=str(cd_pgr_sr0)
        #rez_id_sr1=str(cd_pgr_sr1)
        if len(rez_id_sr0)>5:
            os.system("cd /home/; sudo touch temp.txt; sudo chmod -R ugo+rw /home/temp.txt")#Plik do wyslania listy utworow
            paranoia= subprocess.Popen('sudo cdparanoia -Q 2>&1 | tee /home/temp.txt',shell=True, stdout=subprocess.PIPE)
            
        elif len(rez_id_sr0)<4: 
            messagebox.showinfo("Koniec", "Blad napedu")   
                
        #print(paranoia.communicate()[0])
        nameee="temp.txt"  
        localll= "/home"  
        dcl=os.path.join(localll, nameee)
        temp=open(dcl, "r")
        resolution=temp.read()

          
            
        
            
        cdpara.set(resolution)# Lista tytulow bez nazw  
    except:
        messagebox.showinfo("Koniec","Niespodziewany blad")

load=Button(root, text="ZALADUJ LISTE UTWOROW", command=load, background="white")
load.place(x=55, y=340)










root.eval('tk::PlaceWindow . center')

if sys.version_info[0] <3:
    raise Exception("Wymagany Python3")
    print("Check")

os.system("cd /home/; sudo touch Plik_konfiguracyjny.txt; sudo chmod -R ugo+rw /home/Plik_konfiguracyjny.txt")






res=img.resize((170, 140), Image.ANTIALIAS)
cel =ImageTk.PhotoImage(res)
label2=Label(root, image=cel, width=170, height=140)

label2.place(x=720, y=30)
current=Label(root, text="OBECNA SCIEZKA:", font=("Helvetica", 18))
current.place(x=60, y=50)


varr=StringVar()
labelu=Label(root,textvariable=varr, font=("Helvetica", 18), fg="black")
labelu.place(x=300, y=50)
varr.set("Obecna sciezka domyslna to: /home")

# Zapis numeru pid skryptu glownego, w celu nadpisania pliku conf, zewnetrznym programem.
pid=os.getpid()
pid_2=str(pid)
os.system(" cd /home; sudo touch pid.txt; sudo chmod -R ugo+rw /home/pid.txt")
pid_name="pid.txt"  
whereis="/home"  
plex=os.path.join(whereis, pid_name)
tste=open(plex, "wt")
tste.write(pid_2)
tste.close()
print(pid_2)
actual=os.path.dirname(os.path.realpath(sys.argv[0]))
print(type(actual))
acoman="python3 adding.py"
sudocoman="cd"+" "+actual
os.chdir(actual)
join=[sudocoman, acoman]
print(acoman, sudocoman)
#adding=subprocess.Popen(["cd" +actual+ "sudo", "python3","adding.py"],  stdout=subprocess.PIPE) 
adding=subprocess.Popen(["sudo", "python3", "adding.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#execfile("/home/pi/Final/adding.py")
# os.system("cd /home/pi; python3 adding.py")

# subprocess.call("cd /home/pi; python3 adding.py", shell=True) #Wywowalanie programu nadpisujacego plik conf, przy calkowitym zakonczeniu
   
# exec(open("/home/pi/adding.py").read())





                
                
var1=IntVar()
var2=IntVar()


def usun():
    global folder
    folder=filedialog.askdirectory(initialdir="/home", title="WYBIERZ FOLDER GLOWNY")
    ok.deselect()
    os.chdir(folder)

    
  
def zapisz():
    global docel
    name="Plik_konfiguracyjny.txt"  
    local= "/home"  
    docel=os.path.join(local, name)
    te=open(docel, "w")
    te.write(folder)
    varr.set(folder)
    usun.deselect()
    print(te)

def open_pop():  #Pierwsze okno wyboru sciezki
    root.withdraw()
    global zawar
    
    def default():
        varr.set("/home/usr")
        top.destroy()
        
        time.sleep(0.3)
        root.deiconify()
        os.chdir("/home")
    def zpliku():
        te=open(docel, "r")
        file=te.read()
        
        varr.set(file)
        os.chdir(file)
        root.deiconify()
        top.destroy()
        time.sleep(0.3)
        root.deiconify()
   
    top=Toplevel(root)
    w2=400
    h2=400
    ws2=top.winfo_screenwidth()
    hs2=top.winfo_screenheight()
    x2= (ws2/2) - (w2/2)
    y2= (hs2/2) - (h2/2)
    top.geometry('%dx%d+%d+%d' % (w2, h2, x2, y2))
    
    top.title("WYBIERZ KATALOG")
    dovar=IntVar()
    zawar=IntVar()
    domysl = Checkbutton(top, text="Wybierz sciezke domyslna", variable=dovar, onvalue=1, command=default, offvalue=0,  indicator=0, background="light blue", cursor="hand2", borderwidth=10)
    domysl.pack()
   
    
    var=StringVar()
    var2=StringVar()
    domy=Label(top, textvariable=var,font=("Arial", 18), fg="brown")
    
    var.set("/home/usr")
    name="Plik_konfiguracyjny.txt"  
    local= "/home"  
    docel=os.path.join(local, name)
    te=open(docel, "r")
    file=te.read()
    print(file)
    domy.place(x=120, y=60)
    zawartosc = Checkbutton(top, text="Wybierz poprzednia sciezke uzytkownika", variable=zawar, command=zpliku, onvalue=1,  offvalue=0,  indicator=0, background="light blue", cursor="hand2", borderwidth=10)
    zawartosc.place(x=60, y=160)
    aktu=Label(top, textvariable=var2, fg="brown",font=("Arial", 18))
    
    var2.set(file)#Zawartosc pliku tekstowego
    aktu.place(x=120, y=220)
    if os.path.getsize("/home/Plik_konfiguracyjny.txt") <1:
        zawartosc["state"]= DISABLED
    top.protocol("WM_DELETE_WINDOW", destroy)
    Bcanc=Button(top, text="ZAKONCZ", command=destroy, width=8, height=2, background="orange", cursor="hand2")
    Bcanc.pack(side=BOTTOM)

open_pop()




ok = Checkbutton(root, text="ZAPISZ SCIEZKE", variable=var1, onvalue=1,  offvalue=0, command=zapisz, indicator=0, background="light blue", cursor="hand2", borderwidth=10)
ok.select()
ok.pack(side=LEFT)

usun = Checkbutton(root, text="USUN SCIEZKE", variable=var2, onvalue=1, offvalue=0,command=usun,  indicator=0, background="light blue", cursor="hand2", borderwidth=10)

usun.pack(side=RIGHT)



if var1.get()==1:
    name="Plik_konfiguracyjny.txt"  
    local= "/home"  
    docel=os.path.join(local, name)
    te=open(docel, "r")
    file=te.read()
    


    
    
Acanc=Button(root, text="ZAKONCZ", command=destroy, width=8, height=2, background="orange", cursor="hand2")
Acanc.pack(side=TOP)




    
    
def automat():  # Nadpisuje pierwszy-oryginalny plik formatem FLAC i ejectcd-zawsze przy starcie, na poczatku programu.
    os.system("sudo chmod -R ugo+rw /etc/abcde.conf")
    name="abcde.conf"  
    local= "/etc"  
    docel=os.path.join(local, name)
    te=open(docel, "rt")

    data = te.read()
    data = data.replace("#OUTPUTTYPE=ogg", "OUTPUTTYPE=flac")
    data = data.replace("#EJECTCD=y", "EJECTCD=y")
    data = data.replace('#CDDBCOPYLOCAL="n"', 'CDDBCOPYLOCAL="y"')
    data = data.replace('#CDDBLOCALDIR="$HOME/.cddb"', 'CDDBLOCALDIR="$HOME"')
    #data = data.replace('#CDROM=/dev/cdrom', 'CDROM=/dev/sr0')

    te.close()

    te=open(docel, "wt")

    te.write(data)

    te.close()

    os.system(" cd /etc/; sudo touch kopia_flac.conf; sudo chmod -R ugo+rw /etc/kopia_flac.conf")# Tutaj plik zapisywany jest w celu pozniejszych zmian formatu
    nahme="kopia_flac.conf" 
    gdzie= "/etc"  
    mult=os.path.join(gdzie, nahme)
    do=open(mult, "wt")
    do.write(data)
    

automat()

    
def ogg():
    
    name="abcde.conf"  
    local= "/etc"  
    docel=os.path.join(local, name)
    te=open(docel, "rt")

    data = te.read()
    data = data.replace('OUTPUTTYPE=flac', 'OUTPUTTYPE=ogg')

    te.close()

    te=open(docel, "wt")

    te.write(data)

    te.close()
    ogg["state"]= DISABLED
    MP3["state"]= DISABLED
    flac["state"]= DISABLED
def mp3():
    
    name="abcde.conf"  
    local= "/etc"  
    docel=os.path.join(local, name)
    te=open(docel, "rt")

    data = te.read()
    data = data.replace('OUTPUTTYPE=flac', 'OUTPUTTYPE=mp3')

    te.close()

    te=open(docel, "wt")

    te.write(data)

    te.close()
    ogg["state"]= DISABLED
    MP3["state"]= DISABLED
    flac["state"]= DISABLED
    
def flac():
    ogg["state"]= DISABLED
    MP3["state"]= DISABLED
    flac["state"]= DISABLED
    
flavar=IntVar()
mpvar=IntVar()
oggvar=IntVar()
flac= Checkbutton(root, text="Format FLAC", variable=flavar, onvalue=1, command=flac,  offvalue=0,  indicator=0, background="light blue", cursor="hand2", borderwidth=10)
flac.place(x=100, y=200)
ogg= Checkbutton(root, text="Format OGG", variable=oggvar, onvalue=1, command=ogg,  offvalue=0,  indicator=0, background="light blue", cursor="hand2", borderwidth=10)
ogg.place(x=100, y=150)
MP3= Checkbutton(root, text="Format MP3  ", variable=mpvar, onvalue=1, command=mp3, offvalue=0,  indicator=0, background="light blue", cursor="hand2", borderwidth=10)
MP3.place(x=100, y=250)


def reset(): #Pobieram plik kopii(tylko ze zmienionym formatem, (ejectcd-zostaje) i wklejam ja do glownych ustawien. Reset czyli--
    nahme="kopia_flac.conf"
    gdzie= "/etc"  
    mult=os.path.join(gdzie, nahme)
    do=open(mult, "rt")
    ft2=do.read()
    
    
    name="abcde.conf"  
    local= "/etc"  
    docel=os.path.join(local, name)
    te=open(docel, "wt")

    te.write(ft2)
    ogg["state"]= NORMAL
    MP3["state"]= NORMAL
    flac["state"]= NORMAL
    flavar.set(0)
    mpvar.set(0)
    

Reset=Button(root, text="RESETUJ USTAWIENIA", command=reset, background="white", cursor="hand2")

Reset.place(x=70, y=300)

        






napis=""

def okno_abcde():  # Okno pokazuje rodzaj formatu i przycisk "OK" startujacy program.
    
    try:
        
        
        global napis
        info=Toplevel(background="white")
        w=400
        h=100
        ws=info.winfo_screenwidth()
        hs=info.winfo_screenheight()
        x= (ws/2) - (w/2)
        y= (hs/2) - (h/2)
        info.geometry('%dx%d+%d+%d' % (w, h, x, y))
        info.title("INFORMACJA")
        
        varie=StringVar()
        defa=Label(info, textvariable=varie, background="white", font=("Arial", 12, 'bold'))
        defa.place(x=50, y=20)
    
        with open('/etc/abcde.conf') as f:   #Test czy plik zawiera string, z jakim formatem.
            if "OUTPUTTYPE=flac" in f.read():
                varie.set("Wybrano format Flac, kontynuowac?")
        with open('/etc/abcde.conf') as f:
            if "OUTPUTTYPE=ogg" in f.read():
                varie.set("Wybrano format Ogg, kontynuowac?")
        with open('/etc/abcde.conf') as f:
            if "OUTPUTTYPE=mp3" in f.read():
                varie.set("Wybrano format MP3, kontynuowac?")
        def kill():
                info.destroy()
                info.update()
                
        pgrep= Popen(['blockdev', '--getsize64', '/dev/sr0'],  stdout=subprocess.PIPE) #Sprawdzenie czy cd rom mounted
    
    
        wynik_pgr=pgrep.stdout.read()
        rezultat=str(wynik_pgr)
        print(type(wynik_pgr))
        
        
        
        def check():
            kill()
            
            
            print(rezultat)
            print(rezultat)
            
             #Dalej nie  potrzebuje okna info.
            if len(rezultat)>5: #Sprawdzenie czy plyta w napedzie
                #exec(open("./canc_test.py").read
                
                global napis
               
                
                print(os.getcwd())# Directory moge zmienic tylko po komendzie abcde, bo wczesniej jest ustawiony przez uzyt. inny dir.
        
                sudocoman="cd"+" "+actual
                proc=Popen(['sudo','abcde', '-N'],  stdin=None, stdout=None, stderr=None, close_fds=True)# Program nie czeka az zakonczy sie ten proces.
                
                os.chdir(actual)
                
                can=subprocess.Popen(["sudo", "python3", "can.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                
                
                
                proc.wait()
                print(proc.wait())
                print("Completed")
                os.system("sudo pkill -f  can.py")
                messagebox.showinfo("Koniec", "Koniec")
                
            
            elif len(rezultat)<4:
                
                messagebox.showinfo("CD-ROM","CD rom not loaded")
                info.destroy() 
                
      
        
                    
        
            
        






        
        
        checka=Button(info, text="OK", command=check, cursor="hand2")
        checka.place(x=150, y=60)
    except:
        messagebox.showinfo("Error","Nastapil nieoczekiwany blad")
        destroy()
        sys.exit()
        
            

        
    


    
        
        
            


    
    

rozpocznij=Button(root, text="ROZPOCZNIJ KOPIOWANIE", command=okno_abcde,background="green", fg="white", font=("Arial", 12, 'bold'), cursor="hand2")
rozpocznij.place(x=40, y=450)

    
    
    




   


    
root.protocol("WM_DELETE_WINDOW", destroy)

pid=os.getpid()

print(pid)
    
atexit.register(print, "Exit")

root.mainloop()
