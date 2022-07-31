#Libraries for create window
import tkinter as tk
#Libraries for run command
import subprocess

#Create window
window = tk.Tk()
#Dimensional window 
window.geometry("800x500")
#Title window
window.title("poweroffer")
window.configure(background="blue")
window.grid_columnconfigure(0, weight=1) 

#Welcome text
scritta = tk.Label(window, text="Welcome!", font=("Helvetica",15)) 
scritta.grid(row=0, column=0,  sticky="N", padx=20, pady=10)      
sito = tk.StringVar
text_input= tk.Entry(textvariable=sito)
text_input.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

#Function for shutdown PC
def spegni():
    subprocess.run('shutdown now', shell=True)
    subprocess.run('shutdown -s -t O', shell=True)

#Function for shutdown PC when you visit YouTube and add website
def smetti():
    sito = text_input.get() 
    print(sito)
    #Create siti.dat to save the sites to be checked, if you visit one of the sites listed, turn off your computer.
    f = open ("siti.dat","w")
    f.write(sito)
    f.close()
    #Read and save history web and if you visit one of the listed sites, turn off your computer.
    a = open("executable.py","w")
    a.write("#!/usr/bin/env python3 \n")
    a.write("import os,json,lz4.block,time \n")
    a.write("f = open(\"siti.dat\",\"r\") \n")
    a.write("sito = f.read()\n")
    a.write("d = open(\"/home/usr/snap/firefox/common/.mozilla/firefox/8gnxd9f4.default/sessionstore-backups/recovery.jsonlz4\", \"rb\") \n")
    a.write("magic = d.read(8)\n")
    a.write("data = json.loads(lz4.block.decompress(d.read()).decode(\"utf-8\"))\n")
    a.write("d.close()\n")
    a.write("current_window = \"\"\n")
    a.write("for win in data.get(\"windows\"):\n")
    a.write("   for tab in win.get(\"tabs\"):\n")
    a.write("       i = int(tab.get(\"index\")) - 1 \n")
    a.write("       current_window = tab.get(\"entries\")[i].get(\"url\")\n")
    a.write("print(current_window)\n")
    a.write("if sito in str(current_window):\n")
    a.write("   print(\"Yes\")\n")
    a.write("   os.system(\"shutdown now\")")
    a.close()

    #Create executable.sh for crontab (This way you can run the script every time you start your pc)
    b = open("executable.sh", "w")
    b.write("#!/bin/bash\n")
    b.write("/home/lorenzo/Scrivania/poweroffer/executable.py")
    b.close()

#Stop procrastinating text
second_button= tk.Button(text="Stop procrastinating", command=smetti)
second_button.grid(row=5, column=0, sticky="WE", padx=15, pady=8)

#Have a break from the pc for shutdown PC
first_button = tk.Button(text="have a break from the pc", command=spegni) 
first_button.grid(row=1, column=0, sticky="W", padx=50, pady=50) 

#Always open window
if __name__ == "__main__":
    window.mainloop()