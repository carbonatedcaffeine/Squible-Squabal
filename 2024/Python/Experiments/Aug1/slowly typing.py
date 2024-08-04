# Camden

# Import system and time libraries
from sys import stdout
from time import sleep

# Open a .txt file containing a book.
# In this case is moby dick.
f = open("moby.txt", "r")

# A function that prints text to a screen slowly.
# It works by printing to the standard output and
# flushes the studout every letter at 8ms. This slows down
# the text being printed, therefore making it readable.
def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)

# Read moby.txt and insert it into the print_slow 
# function. The book will then slowly start being printed
# on screen.
print_slow(f.read())

# Close the file when program finishes
f.close