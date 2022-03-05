# Camden Bruce
from cgitb import text
from tkinter import *

def main(): # Run the program
    pack_window()
    main_window.mainloop()

#def append_list():

def pack_window(): # Fills the window with buttons, labels and text entries
#   Label(main_window, text="LOLOLOLOL") .grid(column=1,row=0)  #Deprecated test string
    Button(main_window, text="Quit",command=main_window.destroy) .grid(column=0,row=4)
    Button(main_window, text="Append list") .grid(column=0,row=3)
    Label(main_window, text="Name") .grid(column=1,row=3)
    Label(main_window, text="Receipt number") .grid(column=1,row=4)
    Label(main_window, text="Item code") .grid(column=1,row=5)
    Label(main_window, text="Quantity of item") .grid(column=1,row=6)
    entry_name = Entry(main_window)
    entry_name.grid(column=2,row=3)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=2,row=4)
    entry_item = Entry(main_window)
    entry_item.grid(column=2,row=5)
    entry_item_quantity = Entry(main_window)
    entry_item_quantity.grid(column=2,row=6)

item_codes = {"Camden":"Bruce"}
main_window =Tk()
main()
