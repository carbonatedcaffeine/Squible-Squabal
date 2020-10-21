# Camden Bruce
import tkinter 

def clicked():
    print("click!")

# Create a new window
window = tkinter.Tk()
window.title("Normal window")

# Create the button
my_button = tkinter.Button(window, text="Click me!", command=clicked)
my_button.pack()

# Text
my_label = tkinter.Label(window, text="Some text")
my_label.pack()

# Draw the window and start the application
window.mainloop()