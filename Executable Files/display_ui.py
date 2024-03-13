from tkinter import *
from tkinter import ttk 
# Used for creating a dictionary of user inputs, which will be passed into a CSV writer object
from parse_csv import field_names

class GUI:
    def __init__(self):
        # Main menu portion
        self.root = Tk(className=' Donor Information')
        self.mm_frame = ttk.Frame(self.root, padding=10)
        self.mm_frame.grid()
        self.mm_dm_button = ttk.Button(self.mm_frame, text="Better Unite Template", padding=10, command=lambda: GUI.mm_dm_button_clicked(self))
        self.mm_dm_button.grid(row=0, column=0)
        # Donor menu portion
        self.dm_frame = ttk.Frame(self.root, padding=10)
        self.dm_label_text_var = field_names.pop()
        self.dm_label = ttk.Label(self.dm_frame, text=self.dm_label_text_var, padding=10)
        self.dm_label.grid(row=0, column=0)
        self.dm_entry = ttk.Entry(self.dm_frame)
        self.dm_entry.grid(row=0, column=1)
        self.dm_mm_button = ttk.Button(self.dm_frame, text="Back to Main Menu", padding=10, command=lambda: GUI.dm_mm_button_clicked(self))
        self.dm_mm_button.grid(row=1, column=0)

        self.root.bind('<Return>', GUI.return_key_pressed)
        # Begin displaying GUI
        self.root.mainloop()

    def mm_dm_button_clicked(self):
        self.mm_frame.grid_remove()
        self.dm_frame.grid()

    def dm_mm_button_clicked(self):
        self.dm_frame.grid_remove()
        self.mm_frame.grid()

    def update_dm_frame(self):
        self.dm_label_text_var = field_names.pop()
        self.dm_entry.delete(0, 'end')

    def return_key_pressed(event):
        return ...

def main():
    gui = GUI()

main()