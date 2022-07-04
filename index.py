

from cgitb import text
import tkinter as tk
import subprocess




window = tk.Tk() 
window.geometry("800x500")
window.title("poweroffer")

window.configure(background="blue")


window.grid_columnconfigure(0, weight=1) 

scritta = tk.Label(window, text="Benvenuto nel mio programma!", font=("Helvetica",15)) 
scritta.grid(row=0, column=0,  sticky="N", padx=20, pady=10)      

text_input= tk.Entry()
text_input.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
       

def spegni():
    subprocess.run('shutdown now', shell=True)




first_button = tk.Button(text="Staccati un po' dal pc", command=spegni) 


first_button.grid(row=1, column=0, sticky="W", padx=50, pady=50) 





if __name__ == "__main__":
    window.mainloop()
