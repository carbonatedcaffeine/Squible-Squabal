# Camden Bruce
from ast import While
import curses
from curses.ascii import isdigit
from tkinter import *
from tkinter import messagebox


def main(): # Run the program
    pack_window()
    main_window.mainloop()

def append_list():
    if len(entry_client_name.get())!= 0 :
        j_names.append(entry_client_name.get())
        number_names['total_names'] += 1
    if int(entry_receipt_number.get())!= 0 :
        j_receipts.append(entry_receipt_number.get())
        number_receipts['total_receipt_numbers'] += 1
    if int(entry_item_code.get())!= 0 :
        j_item_codes.append(entry_item_code.get())
        number_item_codes['total_item_codes'] += 1
    if int(entry_item_quantity.get())!= 0 :
        j_item_quantity.append(entry_item_quantity.get())
        number_item_quantity['total_item_quantity'] += 1

def print_variables():
    name_count = 0
    receipt_count = 0
    item_code_count = 0
    item_quantity_count = 0
    ROWS_ABOVE = 3
    while name_count < number_names['total_names']:
        Label(main_window, text=(j_names[name_count])).grid(column=0,row=6+name_count + ROWS_ABOVE)
        name_count += 1
    while receipt_count < number_receipts['total_receipt_numbers']:
        Label(main_window, text=(j_receipts[receipt_count])).grid(column=2,row=6+receipt_count + ROWS_ABOVE)
        receipt_count += 1
    while item_code_count < number_item_codes['total_item_codes']:
        Label(main_window, text=(j_item_codes[item_code_count])).grid(column=4,row=6+item_code_count + ROWS_ABOVE)
        item_code_count += 1
    while item_quantity_count < number_item_quantity['total_item_quantity']:
        Label(main_window, text=(j_item_quantity[item_quantity_count])).grid(column=6,row=6+item_quantity_count + ROWS_ABOVE)
        item_quantity_count += 1

def pack_window(): # Fills the window with buttons, labels and text entries
#   Label(main_window, text="LOLOLOLOL") .grid(column=1,row=0)  #Deprecated test string
    Button(main_window, text="Quit",command=main_window.destroy, width=8, bg='#FF605C', fg='white') .grid(column=0,row=0)
    Button(main_window, text="Append list",command=error_correction, width=8, height=6, bg='#FFBD44', fg='white') .grid(column=0,row=1)
    Button(main_window, text="Print list",command=print_variables, width=8, height=2, bg='#61BB46', fg='white') .grid(column=0,row=2)
    Button(main_window, text="Delete row", width=8, height=2, bg='#51A0D5', fg='white') .grid(column=0,row=4)
    Label(main_window, text="Name") .place(x=170,y=0)
    Label(main_window, text="Receipt number") .place(x=118,y=25)
    Label(main_window, text="Item code") .place(x=148,y=50)
    Label(main_window, text="Quantity of item").place(x=115,y=75)
    Label(main_window, text="Quantity of item").place(x=115,y=75)

    Label(main_window, font='bold',text="  Name  ").grid(column=0,row=5)
    Label(main_window, font='bold',text="  Receipt num  ").grid(column=2,row=5)
    Label(main_window, font='bold',text="  Item code  ").grid(column=4,row=5)
    Label(main_window, font='bold',text="  Item quantity  ").grid(column=6,row=5)
    Label(main_window, font='bold',text="  Row  ").grid(column=8,row=5)

#   Label(main_window, font='bold',text="Row").grid(column=1,row=4)

def error_correction():
#    error_check_failures = 0
    Label(main_window, font='bold', fg='black', text="  Name  ").grid(column=0,row=5)
    Label(main_window, font='bold', fg='black', text="  Receipt num  ").grid(column=2,row=5)
    Label(main_window, font='bold', fg='black', text="  Item code  ").grid(column=4,row=5)
    Label(main_window, font='bold', fg='black', text="  Item quantity  ").grid(column=6,row=5)
    Label(main_window, font='bold', fg='black', text="  Row  ").grid(column=8,row=5)
    
    if len(entry_client_name.get()) !=0 and int(entry_receipt_number.get()) !=0 and int(entry_item_code.get()) !=0 and int(entry_item_quantity.get())  !=0 and entry_receipt_number.get().isdigit() and entry_item_code.get().isdigit and entry_item_quantity.get().isdigit:
       append_list()
    else:
        if len(entry_client_name.get()) == 0:
#            error_check_failures += 1
            Label(main_window, font='bold', fg='red', text="  Name  ").grid(column=0,row=5)
            messagebox.showerror('Inventory program error', 'Error: Missing input in box "Name"')
        
        if entry_receipt_number.get() == 0:
#            error_check_failures += 1
            Label(main_window, font='bold', fg='red', text="  Receipt num  ").grid(column=2,row=5)
            messagebox.showerror('Inventory program error', 'Error: Missing input in box "Receipt number"')

        if entry_item_code.get() == 0:
#            error_check_failures += 1
            Label(main_window, font='bold', fg='red', text="  Item code  ").grid(column=4,row=5)
            messagebox.showerror('Inventory program error', 'Error: Missing input in box "Item code"')

        if entry_item_quantity.get() == 0:
#            error_check_failures += 1
            Label(main_window, font='bold', fg='red', text="  Item quantity  ").grid(column=6,row=5)
            messagebox.showerror('Inventory program error', 'Error: Missing input in box "Item quantity"')
        
#def delete_row():
    
number_names = {'total_names':0}
number_receipts = {'total_receipt_numbers':0}  
number_item_codes = {'total_item_codes':0}
number_item_quantity = {'total_item_quantity':0}

plu_numbers = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
plu_conversions = ["Spoons", "Forks", "Plates", "Knifes", "Teaspoons", "Pots", "Pans", "Bowls", "Cups", "Mugs"]
j_names = []
j_receipts = []
j_item_codes = []
j_item_quantity = []

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
entry_row_number = Entry(main_window, width=3)
entry_row_number.grid(column=1,row=4)

main()