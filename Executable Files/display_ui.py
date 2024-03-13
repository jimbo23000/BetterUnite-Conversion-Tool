from tkinter import *
from tkinter import ttk 
# Used for creating a dictionary of user inputs, which will be passed into a CSV writer object
from parse_csv import field_names

class GUI:
    def __init__(self):
        # Main menu portion
        root = Tk(className=' Donor Information')
        mm_frame = ttk.Frame(root, padding=10)
        mm_frame.grid()
        mm_dm_button = ttk.Button(mm_frame, text="Better Unite Template", padding=10, command=lambda: GUI.mm_dm_button_clicked(self))
        mm_dm_button.grid(row=0, column=0)
        # Donor menu portion
        dm_frame = ttk.Frame(root, padding=10)
        dm_label_text_var = field_names.pop()
        dm_label = ttk.Label(dm_frame, text=dm_label_text_var, padding=10)
        dm_label.grid(row=0, column=0)
        dm_entry = ttk.Entry(dm_frame)
        dm_entry.grid(row=0, column=1)
        dm_mm_button = ttk.Button(dm_frame, text="Back to Main Menu", padding=10, command=lambda: GUI.dm_mm_button_clicked(self))
        dm_mm_button.grid(row=1, column=0)

        root.bind('<Return>', GUI.return_key_pressed)
        
        self.root = root
        self.mm_frame = mm_frame
        self.mm_dm_button = mm_dm_button
        self.dm_frame = dm_frame
        self.dm_label_text_var = dm_label_text_var
        self.dm_label = dm_label
        self.dm_entry = dm_entry
        self.dm_mm_button = dm_mm_button
        # Begin displaying GUI
        root.mainloop()

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