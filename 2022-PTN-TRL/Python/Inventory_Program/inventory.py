# Camden Bruce 2022
from tkinter import *
from tkinter import messagebox
def main(): # Pack the window with buttons and display the window.
    pack_window()
    main_window.mainloop()

def print_variables():
    # Prints the variables that were appended to the list of inputs.
    name_count = 0
    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=10,row=name_count+8)
        Label(main_window, text=(inventory_details[name_count][0])).grid(column=2,row=name_count+8)
        Label(main_window, text=(inventory_details[name_count][1])).grid(column=4,row=name_count+8)
        Label(main_window, text=(inventory_details[name_count][2])).grid(column=6,row=name_count+8)
        Label(main_window, text=(inventory_details[name_count][3])).grid(column=8,row=name_count+8)
        name_count += 1
        counters['name_count'] = name_count

def append_list():
        # If inputs pass the error_correction test it will append each input to a list. Places 0, 1, 2, 3 respectively.
        inventory_details.append([entry_client_name.get(),entry_receipt_number.get(),entry_item_code.get(),entry_item_quantity.get()])
        entry_client_name.delete(0,'end')
        entry_receipt_number.delete(0,'end')
        entry_item_code.delete(0,'end')
        entry_item_quantity.delete(0,'end')
        counters['total_entries'] += 1
        
def pack_window(): # Fills the window with buttons, labels and text entries
    Button(main_window, text="Quit",command=main_window.destroy, width=8, bg='#FF605C', fg='white') .grid(column=0,row=0)
    Button(main_window, text="Append list",command=error_correction, width=8, height=6, bg='#FFBD44', fg='white') .grid(column=0,row=1)
    Button(main_window, text="Print list",command=print_variables, width=8, height=2, bg='#61BB46', fg='white') .grid(column=0,row=2)
    Button(main_window, text="Delete row",command=delete_row, width=8, height=2, bg='#51A0D5', fg='white') .grid(column=0,row=4)
    Label(main_window, text="Name") .place(x=170,y=0)
    Label(main_window, text="Receipt number") .place(x=118,y=25)
    Label(main_window, text="Item code") .place(x=148,y=50)
    Label(main_window, text="Quantity of item").place(x=115,y=75)
    Label(main_window, text="Quantity of item").place(x=115,y=75)

    Label(main_window, font='bold',text="   Name  ").grid(column=2,row=5)
    Label(main_window, font='bold',text="  Receipt num  ").grid(column=4,row=5)
    Label(main_window, font='bold',text="  Item code  ").grid(column=6,row=5)
    Label(main_window, font='bold',text="  Item quantity  ").grid(column=8,row=5)
    Label(main_window, font='bold',text="  Row").grid(column=10,row=5)

def error_correction():
    # Initialize error count to 0 and refresh text box labels to default colour (black).
    missing_inputs = 0
    non_int_inputs = 0
    Label(main_window, fg='black', text="Name") .place(x=170,y=0)
    Label(main_window, fg='black', text="Receipt number") .place(x=118,y=25)
    Label(main_window, fg='black', text="Item code") .place(x=148,y=50)
    Label(main_window, fg='black', text="Quantity of item").place(x=115,y=75)


    # If an integer input has a alphabet character prompt an errorbox and mark input box green. 
    if str(entry_receipt_number.get()).isdigit() == False:
        non_int_inputs = 1
        Label(main_window, fg='green', text="Receipt number") .place(x=118,y=25)
    if str(entry_item_code.get()).isdigit() == False:
        non_int_inputs = 1
        Label(main_window, fg='green', text="Item code") .place(x=148,y=50)
    if str(entry_item_quantity.get()).isdigit() == False:
        non_int_inputs = 1
        Label(main_window, fg='green', text="Quantity of item").place(x=115,y=75)
    
    # If the length of the string of an input is 0, or in simpler terms if there is nothing in an input box then prompt an errorbox and mark input box red.
    if len(entry_client_name.get()) == 0:
        missing_inputs = 1
        Label(main_window, fg='red', text="Name") .place(x=170,y=0)
    if len(entry_receipt_number.get()) == 0:
        missing_inputs = 1
        Label(main_window, fg='red', text="Receipt number") .place(x=118,y=25)
    if len(entry_item_code.get()) == 0:
        missing_inputs = 1
        Label(main_window, fg='red', text="Item code") .place(x=148,y=50)
    if len(entry_item_quantity.get()) == 0:
        missing_inputs = 1
        Label(main_window, fg='red', text="Quantity of item").place(x=115,y=75)
    # If an error is found through the check it will prompt one of these error boxes. 
    # It will mark a different colour according to the error type.
    if missing_inputs == 1:
        messagebox.showerror('Inventory program error', 'Error: missing input. Errors highlighed in red')
    if non_int_inputs == 1:
        messagebox.showerror('Inventory program error', 'Error: non integer input. Errors highlighted in green')
    else:
        append_list()
def delete_row():
    # Delete a row from an integer input, row numbers start from 0. Then labels are wiped with spaces, which isn't very efficient.
    # But to be fair i'm not entirely sure how else to do it.
    del inventory_details[int(entry_row_number.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    entry_row_number.delete(0,'end')
    Label(main_window, text="                           ").grid(column=2,row=name_count+7) 
    Label(main_window, text="                           ").grid(column=4,row=name_count+7)
    Label(main_window, text="                           ").grid(column=6,row=name_count+7)
    Label(main_window, text="                           ").grid(column=8,row=name_count+7)
    Label(main_window, text="                           ").grid(column=10,row=name_count+7)
    print_variables()

# Initialize input boxes, tk window elements and optional window geometry.
# Uncomment window geometry and resizable options for the older interface size (deprecated). 
counters = {'total_entries':0,'name_count':0}
inventory_details = []
main_window = Tk()
main_window.title('Stock inventory')
#main_window.geometry('600x300')
#main_window.resizable(False, True)
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

# Run the program
main()