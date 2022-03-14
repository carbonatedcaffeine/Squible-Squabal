# Camden Bruce
from tkinter import *
from tkinter.tix import COLUMN
from turtle import width

def main(): # Run the program
    pack_window()
    main_window.mainloop()

def append_list():
    if len(entry_client_name.get())!= 0 :
        j_names.append(entry_client_name.get())
        number['total_names'] += 1
    if len(entry_client_receipt.get())!= 0 :
        j_names.append(entry_client_receipt.get())
        number['total_receipt_numbers'] += 1

def print_variables():
    name_count = 0
    receipt_count = 0
    Label(main_window, font='bold',text="Name").grid(column=0,row=5)
    Label(main_window, font='bold',text="Receipt num").grid(column=0,row=6)
    ROWS_ABOVE = 3
    while name_count < number['total_entries']:
        Label(main_window, text=(j_names[name_count])).grid(column=0,row=6 + ROWS_ABOVE)
        name_count += 1

def pack_window(): # Fills the window with buttons, labels and text entries
#   Label(main_window, text="LOLOLOLOL") .grid(column=1,row=0)  #Deprecated test string
    Button(main_window, text="Quit",command=main_window.destroy, width=8, bg='#FF605C', fg='white') .grid(column=0,row=0)
    Button(main_window, text="Append list",command=append_list, width=8, height=6, bg='#FFBD44', fg='white') .grid(column=0,row=1)
    Button(main_window, text="Print list",command=print_variables, width=8, height=2, bg='#61BB46', fg='white') .grid(column=0,row=2)
    Button(main_window, text="Delete row", width=8, height=2, bg='#51A0D5', fg='white') .grid(column=0,row=4)
    Label(main_window, text="Name") .place(x=170,y=0)
    Label(main_window, text="Receipt number") .place(x=118,y=25)
    Label(main_window, text="Item code") .place(x=148,y=50)
    Label(main_window, text="Quantity of item").place(x=115,y=75)
    Label(main_window, text="Quantity of item").place(x=115,y=75)



number = {'total_entries':0}
j_names = []


main_window = Tk()
main_window.title('Stock inventory')
main_window.geometry('600x300')
main_window.resizable(False, True)
entry_client_name = Entry(main_window, width=38)
entry_client_name.place(x=220,y=0)
entry_receipt_number = Entry(main_window, width=38)
entry_receipt_number.place(x=220,y=25)
entry_item_code = Entry(main_window, width=38)
entry_item_code.place(x=220,y=50)
entry_item_quantity = Entry(main_window, width=38)
entry_item_quantity.place(x=220,y=75)
main()

