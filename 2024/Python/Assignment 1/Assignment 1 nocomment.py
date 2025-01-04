# Camden - 2024

from glob import glob
from sys import stdout
from time import sleep
import os

def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)

def error_correct(user_input:str,book_list:str):
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
    print(f'\n{" Camdens book reader ":#^57}',"""\n
Welcome to Camdens book reader, you can start reading 
by typing in a number corresponding to a book below 
and pressing enter/return on your keyboard.
          
Please make sure you are running this program from it's directory.\n""")
    
    book_list = [os.path.basename(x) for x in (glob("books/*.txt"))]
    for book_index in range(len(book_list)):
        print(book_index,".",book_list[book_index])

    user_input = (input("\nType in a number or type 'exit' > "));error_correct(user_input,book_list)
    chosen_book = open("books/" + book_list[int(user_input)], "r")
    print_slow(chosen_book.read())
    
    chosen_book.close

# Run forrest run!
main()