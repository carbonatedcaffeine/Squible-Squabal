# Camden Bruce
from cgitb import text
from tkinter import *

def main():
    pack_buttons()
    main_window.mainloop()

def quit():
    main_window.destroy()

def pack_buttons():
    Button(main_window, text="Quit",command=quit) .grid(column=0,row=2)

item_codes = {"Camden":"Bruce"}
main_window =Tk()
main()
