# Camden
from glob import glob
from sys import stdout
from time import sleep
def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)
booklist = (glob("books/*.txt"))
for bookorder in range(len(booklist)):
    print(bookorder,".",booklist[bookorder])
chosenbook = open(booklist[int(input("> "))], "r")
print_slow(chosenbook.read())
chosenbook.close