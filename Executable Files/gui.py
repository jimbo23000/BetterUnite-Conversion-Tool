from tkinter import *
from tkinter import ttk
from glob import glob
from os import path
import parse

class GUI:
    # Instantiate GUI root and main menu frame
    def __init__(self, csv_src_path, csv_dst_path):
        self.root = root = Tk(className=' Donor Information')
        self.csv_src_path = csv_src_path
        self.csv_dst_path = csv_dst_path
        # Dynamically creates the main menu based on the number of templates
        GUI.create_main_menu(self)
        # Begin displaying GUI
        root.mainloop()

    # Creates the main menu frame, which is placed on top of root
    def create_main_menu(self):
        self.main_menu_frame = main_menu_frame = ttk.Frame(self.root, padding=10)
        main_menu_frame.grid()
        csv_src_path = self.csv_src_path
        i, j = 0, 0
        for file_path in glob(csv_src_path + '/*.csv'):
            if (j > 3):
                i += 1
                j -= j
            else:
                j += 1
            # TODO: Format the text field to exclude the '.csv'
            ttk.Button(main_menu_frame, text=path.basename(file_path), padding=10, command=lambda: GUI.donor_menu_clicked(self, file_path)).grid(row=i, column=j)

    # Creates the donor menu frame, which is placed on top of root
    def create_donor_menu(self):
        root = self.root
        self.donor_menu_frame = donor_menu_frame = ttk.Frame(root, padding=10)
        self.donor_menu_label = donor_menu_label = ttk.Label(donor_menu_frame, text=self.keys[self.keys_index], padding=10)
        donor_menu_label.grid(row=0, column=0)
        self.donor_menu_entry = donor_menu_entry = ttk.Entry(donor_menu_frame)
        donor_menu_entry.grid(row=0, column=1)
        self.back_button = back_button = ttk.Button(donor_menu_frame, text="Back", padding=10, command=lambda: GUI.back_clicked(self))
        back_button.grid(row=1, column=0)
        self.next_button = next_button = ttk.Button(donor_menu_frame, text="Next", padding=10, command=lambda: GUI.next_clicked(self))
        next_button.grid(row=1, column=1)
        self.save_button = save_button = ttk.Button(donor_menu_frame, text="Save", padding=10, command=lambda: GUI.save_clicked(self))
        save_button.grid(row=1, column=2)
        def return_key_pressed(event):
            GUI.update_donor_menu(self)
        root.bind('<Return>', return_key_pressed)

    # Updates the donor menu frame during data entry
    def update_donor_menu(self):
        self.values.append(self.donor_menu_entry.get())
        if (self.keys_index >= self.keys_length - 1):
            csv_row_entry = {self.keys[i]: self.values[i] for i in range(len(self.values))}
            self.csv_row_entries.append(csv_row_entry)
            self.keys_index = 0
            self.values.clear()
        else:
            self.keys_index += 1
        self.donor_menu_label.configure(text=self.keys[self.keys_index])
        self.donor_menu_entry.delete(0, 'end')

    # Call the creation of a new donor menu frame based on the template selected
    def donor_menu_clicked(self, filename):
        # Instantiate the key and dictionary variables
        self.keys = keys = parse.create_keys(filename)
        self.keys_index = 0
        self.keys_length = len(keys)
        self.values = list()
        self.csv_row_entries = list()
        GUI.create_donor_menu(self)
        # Removes, but preserves widget layout of the main menu frame
        self.main_menu_frame.grid_remove()
        self.donor_menu_frame.grid()

    # Removes, but preserves widget layout of the donor menu frame
    def back_clicked(self):
        # TODO: Add a cache for already created donor menu frames next update
        self.donor_menu_frame.grid_remove()
        self.main_menu_frame.grid()

    # Saves CSV row entry and resets values list
    def next_clicked(self):
        self.keys_index = self.keys_length - 1
        GUI.update_donor_menu(self)

    # Uploads CSV row entries and terminates the program
    def save_clicked(self):
        GUI.next_clicked(self)
        parse.create_output_csv(self.csv_dst_path, self.keys, self.csv_row_entries)
        # TODO: Need to migrate exit to a seperate button next update
        self.root.destroy()