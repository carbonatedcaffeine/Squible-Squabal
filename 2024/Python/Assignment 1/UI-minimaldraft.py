# Camden - 2024
from glob import glob
from sys import stdout
from time import sleep
def print_slow(str):
    for letter in str:
        stdout.write(letter);stdout.flush();sleep(0.04)
def error_correct(user_input,book_list):
        if user_input == "":
            return
        if user_input.isdigit() and int(user_input) <= len(book_list)-1:
            return
        else:
            exit()
def main():        
    book_list = (glob("books/*.txt"))
    for book_order in range(len(book_list)):
        print(book_order,".",book_list[book_order])    
    user_input = (input("\n> "))
    error_correct(user_input,book_list)
    chosen_book = open(book_list[int(user_input)], "r")
    print_slow(chosen_book.read());chosen_book.close
main()