class Library:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name.upper()
        self.book_data={}
        self.lendedbook=[]

    def display_book(self):
        print("\n")
        for index,books in enumerate(self.book_list,start=1):
            print(f"{index}:{books}")
        print("\n\n")

    def add_book(self):
        while (True):
            book = input("\nEnter a book name")
            self.book_list.append(book)
            a = input("Do you want to add more book? (Y/N)").upper()
            if a == "Y":
                continue
            else:
                break
        self.book_data[book]=None
        print("Thanks for your contribution")

    def lend_book(self):
        book = input("Enter book name")
        if book not in self.book_list:
            print("Invalid name of book/Book is not available")
        if book in self.book_list:
            if book in self.lendedbook:
                print("Book is already lended")
            else:
                name = input("Enter your name").upper()
                self.book_data[book] = name
                self.lendedbook.append(book)

    def return_book(self):
        name = input("Enter your name").upper()

        for key, value in self.book_data.items():
            if value != None:
              if value == name:
                print(key, value)
                self.book_data[key] = None
                print(f"Book: {key} return successfull")
                self.lendedbook.remove(key)
                break
              else:
                  print(f"Incorrect name or no book lended to {name}")

    def delete_book(self):
        #book = input("Enter book name to delete")
        while(True):
          book = input("Enter book name to delete")
          try:
            self.book_list.remove(book)
            break
          except:
            print("Please correct book name. Book name is case sensitive")


def main():
    list_of_book = ["Maths", "Physics", "Biology", "Science"]
    library_name = "Romil's Library"
    romillibrary = Library(list_of_book, library_name)
    print(" Welcome to house of books \n")

    exit = False
    while(exit == False):
       choice = input("Select your choice from below:\n1:List of books\n2:Add new book\n3:Lend a book\n4:Return book\n5:Remove a book\nQ:Exit from house ").upper()

       if choice == "1":
           romillibrary.display_book()
       elif choice == "2":
           romillibrary.add_book()
       elif choice == "3":
           romillibrary.lend_book()
       elif choice == "4":
           romillibrary.return_book()
       elif choice == "5":
           romillibrary.delete_book()
       elif choice == "Q":
           exit = True
       else:
           print(" Wrong entry")

if __name__ == '__main__':
    main()



