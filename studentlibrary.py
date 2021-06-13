class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks
        
    def displayAvailableBooks(self):
        print("The books present in the library are :- ")
        for book in self.books:
            print(" .) " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"The book {bookName} is issued. Please return within stipulated time period of 2 weeks.")
            self.books.remove(bookName)
            return True
        else:
            print(f"The requested book {bookName} is not either not available or it is already been issued to someoe else. Please select another book or wait until your requested book is returned.")
            return False


    def returnBook(self, bookName):
        self.books.append(bookName)
        print("The book is returned successfully. We hope you enjoyed reading it.")


class Student:
    def __init__(self):
        self.bookList = []
    
    def requestBook(self):
        self.book = input("Enter the name of the book :- ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return :- ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["C", "C++", "JAVA", "Python", "ML", "Django", "FLask", "mongoDB", "Node.js", "Assembly", "DSA", "Redis"])
    student = Student()

    while(True):
        welcomeMsg = '''   <=======Welcome To Study Library=======>
             Please choose an option:
             1. Press 1 to get the list of all the books.
             2. Press 2 to register for a book.
             3. Press 3 to return a book.
             4. Press 4 to exit.                       

        '''
        print(welcomeMsg)
        a = int(input("Enter your choice :- "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing our library. We hope to see you soon. Have a nice day.")
            exit()
        else:
            print("Sorry to say but you have entered incorrect option. Please choose a correct one.")
        
        

