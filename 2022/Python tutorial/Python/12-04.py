# Camden Bruce
from cgitb import text
from tkinter import *

def quit():
    main_window.destroy()

def main():
    Button(main_window, text="Quit", command=quit) .grid()
    main_window.mainloop()

main_window = Tk()
main()