from tkinter import *
from tkinter import ttk 
from parse_csv import field_names

def execute_mainloop():
    root = Tk(className=' Donor Information')
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text=field_names[0][0]).grid(row=0, column=0)
    ttk.Entry(frame).grid(row=0, column=1)
    ttk.Button(frame, text="Next", command=root.update_idletasks).grid(row=1, column=0)
    ttk.Button(frame, text="Save and Exit", command=root.destroy).grid(row=1, column=1)
    root.mainloop()

def main():
    execute_mainloop()

main()