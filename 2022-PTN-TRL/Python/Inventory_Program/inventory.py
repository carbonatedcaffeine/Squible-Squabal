# Camden Bruce
from tkinter import *
from turtle import width

def main(): # Run the program
    pack_window()
    main_window.mainloop()

#def append_list():

def pack_window(): # Fills the window with buttons, labels and text entries
#   Label(main_window, text="LOLOLOLOL") .grid(column=1,row=0)  #Deprecated test string
    Button(main_window, text="Quit",command=main_window.destroy, width=8, bg='#FF605C', fg='white') .place(x=0, y=0)
    Button(main_window, text="Append list", width=8, height=6, bg='#FFBD44', fg='white') .place(x=0,y=30)
    Button(main_window, text="Print list", width=8, height=2, bg='#61BB46', fg='white') .place(x=0,y=135)
    Button(main_window, text="Delete row", width=8, height=2, bg='#51A0D5', fg='white') .place(x=0,y=180)
    

    Label(main_window, text="Name") .place(x=170,y=0)
    Label(main_window, text="Receipt number") .place(x=118,y=25)
    Label(main_window, text="Item code") .place(x=148,y=50)
    Label(main_window, text="Quantity of item").place(x=115,y=75)
    Label(main_window, text="Quantity of item").place(x=115,y=75)
    entry_client_name = Entry(main_window, width=100)
    entry_client_name.place(x=220,y=0)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.place(x=220,y=25)
    entry_item_code = Entry(main_window)
    entry_item_code.place(x=220,y=50)
    entry_item_quantity = Entry(main_window)
    entry_item_quantity.place(x=220,y=75)

main_window = Tk()
main_window.title('Stock inventory')
main_window.geometry('450x300')
main()

