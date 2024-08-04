# Camden - 2024

from glob import glob
from sys import stdout
from time import sleep

def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)

def error_correct(user_input,book_list):
        if user_input == "":
            main()
        if user_input.isdigit() and int(user_input) <= len(book_list)-1:
            #print("Error correction returned true")
            return
        else:
            #print("Error correction returned false")
            print(f'\n{" Oops :( ":#^57}',"""\n
ERROR: Incorrect input, did you accidentally 
enter a number for a book that doesn't exist
or enter non numerical character?\n""",f'\n{" Oops :( ":#^57}\n')
            sleep(3);main()

def main():        
    print(f'\n{" Camdens book reader ":#^57}',"""\n
Welcome to Camdens book reader, you can start reading 
by typing in a number corresponding to a book below 
and pressing enter/return on your keyboard.\n""")
    
    book_list = (glob("books/*.txt"))
    for book_order in range(len(book_list)):
        print(book_order,".",book_list[book_order],)
    
    user_input = (input("\n> "));error_correct(user_input,book_list)
    chosen_book = open(book_list[int(user_input)], "r")
    print_slow(chosen_book.read());chosen_book.close

# Run forrest run!
main()