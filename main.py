#Libraries for create a window
import tkinter as tk
#Libraries for execute command
import subprocess
#Libraries for read web browser history
from browser_history import get_history
#Libraries for date time
from datetime import datetime
#Libraries for read csv
import csv

#Print all browser history on cvs
outputs = get_history()
outputs.save("history.csv")

#Get current date
now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d %H:%M")
print('DateTime String:', date_time_str)

#Search Youtube Link on history.csv
how_to_search = 'https://www.youtube.com/'
rows = []
with open('history.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',')
     for line in reader:
        if how_to_search in line:
            print("Yes!")

#Create a window
window = tk.Tk()
#Resolution program
window.geometry("800x500")
#Title program
window.title("Poweroffer")
#Background program
window.configure(background="blue")
window.grid_columnconfigure(0, weight=1) 

#Welcome text
scritta = tk.Label(window, text="Welcome!", font=("Helvetica",15)) 
scritta.grid(row=0, column=0,  sticky="N", padx=20, pady=10)      

sito = tk.StringVar
text_input= tk.Entry(textvariable=sito)
text_input.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

#Button stop procrastinating
second_button= tk.Button(text="Stop procrastinating")
second_button.grid(row=5, column=0, sticky="WE", padx=15, pady=8)

#Button for shutdown pc
first_button = tk.Button(text="have a break from the pc") 
first_button.grid(row=1, column=0, sticky="W", padx=50, pady=50) 

#Always open window
if __name__ == "__main__":
    window.mainloop()