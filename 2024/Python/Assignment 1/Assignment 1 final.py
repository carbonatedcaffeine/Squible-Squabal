# Camden - 2024
# Extra documentation can be found in README.md.

# Import libraries
# glob: finding pathname and file patterns
# sys: to flush the standard output
# time: used for sleep function to wait 
# for a set amount of between printing letters
# os: for handling file names.
from glob import glob
from sys import stdout
from time import sleep
import os

# Function to print the book slowly.
# It loops writing a letter, flushing the
# standard output and sleeping to add a delay
# between printing the letter on the screen.
def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)

# The error correction code for the main program.
# It checks the users input to see if it's an
# integer and checks that the number returned is
# valid (eg. 10 books, user picks 11 or -1, it will fail). 
# I also include a "-1" at the end since lists start
# at 0.
def error_correct(user_input:str,book_list:str):
        # Use checks to see where the code is getting stuck. 
        if user_input.isdigit() and int(user_input) <= len(book_list)-1:
            #print("Error correction completed successfully")
            return
        if user_input == 'exit' or user_input == 'quit':
             exit()
        else:
            #print("Error correction failed")
            print(f'\n{" Oops :( ":#^57}',"""\n
ERROR: Incorrect input, did you accidentally 
enter a number for a book that doesn't exist
or enter non numerical character?\n""",f'\n{" Oops :( ":#^57}\n')
            sleep(3);main()


def main():        
    # A header using formatting, title 
    # text is surrounded by hashes.
    print(f'\n{" Camdens book reader ":#^57}',"""\n
Welcome to Camdens book reader, you can start reading 
by typing in a number corresponding to a book below 
and pressing enter/return on your keyboard.
          
Please make sure you are running this program from it's directory.\n""")
    
    # Checks for text files in the "books" directory 
    # using the wildcard character (*). 
    book_list = [os.path.basename(x) for x in (glob("books/*.txt"))]
    
    # Check if the list is formatted correctly before formatting it.
    # print(book_list)

    # Lists all the books inside the "books" directory.
    # Since "booklist" is just a list, we can use the ammount
    # of books as the range, and it iterates though printing each
    # file in the directory out as it goes through each number in the list.
    for book_index in range(len(book_list)):
        print(book_index,".",book_list[book_index])
    
    # Grab the users input and put it in a variable,
    # then run the error correction code. 
    user_input = (input("\nType in a number or type 'exit' > "));error_correct(user_input,book_list)
    
    # Select the chosen book by using the number input 
    # and using the location in the list to put into
    # a variable. Then open the .txt file as read only.
    chosen_book = open("books/" + book_list[int(user_input)], "r")

    # Print out the chosen book using the "print_slow" 
    # function from earlier.
    print_slow(chosen_book.read())
    
    # Once finished, it's always good practice to release
    # the file. 
    chosen_book.close

# Run forrest run!
main()