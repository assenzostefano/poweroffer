#Libraries for create a window
import tkinter as tk
#Libraries for execute command
import subprocess
#Libraries for read web browser history
from browser_history.browsers import Firefox

#Print all browser history on txt
with open('history.txt', 'w') as f:
    fi = Firefox()
    outputs = fi.fetch_history()
    his = outputs.histories
    for line in his:
        f.write(str(line))
        f.write('\n')

window = tk.Tk() 
#Resolution program
window.geometry("800x500")
#Title program
window.title("Poweroffer")
#Background program
window.configure(background="blue")
window.grid_columnconfigure(0, weight=1) 

scritta = tk.Label(window, text="Welcome!", font=("Helvetica",15)) 
scritta.grid(row=0, column=0,  sticky="N", padx=20, pady=10)      

sito = tk.StringVar
text_input= tk.Entry(textvariable=sito)
text_input.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

#Button stop procrastinating
second_button= tk.Button(text="Stop procrastinating", command=smetti)
second_button.grid(row=5, column=0, sticky="WE", padx=15, pady=8)

#Button for shutdown pc
first_button = tk.Button(text="have a break from the pc", command=spegni) 
first_button.grid(row=1, column=0, sticky="W", padx=50, pady=50) 

#Always open window
if __name__ == "__main__":
    window.mainloop()