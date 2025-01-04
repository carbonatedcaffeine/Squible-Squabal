# Camden
class Book:
    def __init__(self,name,author,publisher,datepublished):
        self.name = name 
        self.publisher = publisher
        self.author = author
        self.datepublished = None
if __name__ == "__main__":
    book1 = Book("Camden's Book","Camden","Camden's publisher","2024")

    print(book1.author)