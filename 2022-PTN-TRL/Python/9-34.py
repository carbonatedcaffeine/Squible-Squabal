# Camden Bruce
from tkinter import *

def quit():
    main_window.destroy()

def print_names():
    name_count = 0
    Label(main_window, font='bold',text="Name").grid(column=0,row=2)
    ROWS_ABOVE = 3
    while name_count < number['total_entries']:
        Label(main_window, text=(j_names[name_count])).grid(column=0,row=name_count + ROWS_ABOVE)
        name_count += 1

def append_name():
    if len(entry_name.get())!= 0 :
        j_names.append(entry_name.get())
        number['total_entries'] += 1

def main():
    Button(main_window, text="Quit",command=quit) .grid(column=1, row=0)
    Button(main_window, text="Append Name",command=append_name) .grid(column=0,row=1)
    Button(main_window, text="Print Names",command=print_names) .grid(column=1,row=1)
    Label(main_window, text="Name") .grid(column=0,row=2)
    main_window.mainloop()

number = {'total_entries':0}
j_names = []
main_window =Tk()
entry_name = Entry(main_window)
entry_name.grid(column=1,row=2)

main()
