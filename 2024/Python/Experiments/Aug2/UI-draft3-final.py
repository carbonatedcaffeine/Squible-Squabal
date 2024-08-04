# Camden
import glob
from sys import stdout
from time import sleep

def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)

print(f'{" Camdens book reader ":#^57}',"""\n
Welcome to Camdens book reader, you can start by typing
in a number corresponding to the book below and pressing 
enter/return on your keyboard.""")
x = (glob.glob("*/*/*.txt"))
# Trying to increment listings.
#for i in y(range(10)):
#    y+1
#    print("1.",x[y])
for n in range(2):
    print(n+1,".",x[n])

f = open(x[int(input("> "))], "r")
print_slow(f.read())