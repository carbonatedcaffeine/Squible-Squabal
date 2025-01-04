# Camden, 2024

# book = user_input in this context, since we call it in the function below.
# Then we open the booklist at the users input. For example book_list[1] = "moby-dick.txt".
# And once we do that we can use f.read to print out the file.
def ChooseBook(book:int):
    f = open(book_list[int(book)], "r")
    print(f.read())

# A list where we can put our book file names. 
# This is static, so the order will never change, maybe
# you can sort it alphabetically? 
book_list = [
    "moby-dick.txt",
    "frankenstein.txt"
]

# Get the users input and put it into variable "user_input"
user_input = input("""
Book Reader
##########################################      
0. Moby Dick
1. Frankenstein

Which book should I choose? > """)

# Insert the users input into the ChooseBook function.
# It will then play the book if it exists. There is no error
# correction code as of yet and will fail if these files do not exist.
ChooseBook(user_input)