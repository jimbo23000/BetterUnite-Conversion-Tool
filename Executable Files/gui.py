from tkinter import *
from tkinter import ttk
import parse

class GUI:
    # Instantiate GUI frames and binding behavior
    def __init__(self, csv_path, keys):
        keys_index = 0

        # Main menu portion
        root = Tk(className=' Donor Information')
        mm_frame = ttk.Frame(root, padding=10)
        mm_frame.grid()
        mm_dm_button = ttk.Button(mm_frame, text="Better Unite Template", padding=10, command=lambda: GUI.mm_dm_button_clicked(self))
        mm_dm_button.grid(row=0, column=0)

        # Donor menu portion
        dm_frame = ttk.Frame(root, padding=10)
        dm_label = ttk.Label(dm_frame, text=keys[keys_index], padding=10)
        dm_label.grid(row=0, column=0)
        dm_entry = ttk.Entry(dm_frame)
        dm_entry.grid(row=0, column=1)
        dm_mm_button = ttk.Button(dm_frame, text="Back to Main Menu", padding=10, command=lambda: GUI.dm_mm_button_clicked(self))
        dm_mm_button.grid(row=1, column=0)
        dm_nd_button = ttk.Button(dm_frame, text="Next Donor", padding=10, command=lambda: GUI.dm_nd_button_clicked(self))
        dm_nd_button.grid(row=1, column=1)
        dm_se_button = ttk.Button(dm_frame, text="Save and Exit", padding=10, command=lambda: GUI.dm_se_button_clicked(self))
        dm_se_button.grid(row=1, column=2)
        
        # Instance variable declarations
        self.root = root
        self.mm_frame = mm_frame
        self.mm_dm_button = mm_dm_button
        self.dm_frame = dm_frame
        self.dm_label = dm_label
        self.dm_entry = dm_entry
        self.dm_mm_button = dm_mm_button
        self.dm_nd_button = dm_nd_button
        self.dm_se_button = dm_se_button

        # Instance variable declarations that enable dictionary creation
        self.csv_path = csv_path
        self.keys = keys
        self.keys_index = keys_index
        self.keys_length = len(keys)
        self.values = list()
        self.csv_row_entries = list()

        # Define this function during initialization, as we need access to the object instance
        def return_key_pressed(event):
            GUI.update_dm_frame(self)
        root.bind('<Return>', return_key_pressed)

        # Begin displaying GUI
        root.mainloop()

    # Switch to donor menu
    def mm_dm_button_clicked(self):
        self.mm_frame.grid_remove()
        self.dm_frame.grid()

    # Switch to main menu
    def dm_mm_button_clicked(self):
        self.dm_frame.grid_remove()
        self.mm_frame.grid()

    # Updates the donor menu
    def update_dm_frame(self):
        self.values.extend(self.dm_entry.get())
        if (self.keys_index >= self.keys_length - 1):
            self.csv_row_entries.extend(dict.fromkeys(self.keys, self.values))
            # Reset for next donor
            self.keys_index = 0
            self.values.clear()
        else:
            self.keys_index += 1
        self.dm_label.configure(text=self.keys[self.keys_index])
        self.dm_entry.delete(0, 'end')

    # Saves CSV row entry and resets values list
    def dm_nd_button_clicked(self):
        self.keys_index = self.keys_length - 1
        GUI.update_dm_frame(self)

    # Uploads CSV row entries and terminates the program
    def dm_se_button_clicked(self):
        parse.create_output_csv(self.csv_path, self.keys, self.csv_row_entries)
        self.root.destroy()