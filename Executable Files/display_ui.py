from tkinter import *
from tkinter import ttk 
# Used for creating a dictionary of user inputs, which will be passed into a CSV writer object
from parse_csv import field_names

# Variable scope is extremely important within this function
def execute_mainloop():
    window = Tk(className=' Donor Information')
    # This frame allows for additional templates to be added in the future
    main_menu = ttk.Frame(window, padding=10)
    main_menu.grid()
    # This is the primary frame all templates will utilize
    donor_info_menu = ttk.Frame(window, padding=10)
    def better_unite_clicked():
        main_menu.grid_remove()
        donor_info_menu.grid()
    ttk.Button(main_menu, text="Better Unite Template", padding=10, command=better_unite_clicked).grid(row=0, column=0)
    input_label = ttk.Label(donor_info_menu, text=, padding=10).grid(row=0, column=0)
    input_entry = ttk.Entry(donor_info_menu).grid(row=0, column=1)
    user_input = StringVar()
    def return_pressed(event):
        user_input.get()
        # Add dictionary implementation
        ttk.Label.config(input_label, text=)
        ttk.Entry.delete(input_entry, 0, 'end')
    window.bind('<Return>', return_pressed)
    window.mainloop()

execute_mainloop()