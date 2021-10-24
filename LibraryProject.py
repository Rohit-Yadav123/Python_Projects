# This is the Library Management Project in python
class Library:
    # Library Constructer
    def __init__(self,list1,name):
        self.bookList=list1
        self.name=name
        self.lendDict={}
    # This Function will show all the book that has been put in the library
    def displayBook(self):
        print(f"We have following books in library:{self.name}")
        for book in self.bookList:
            print(book)
    # This function will show the book that has been taken on lend by user        
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Book Dictionery has been updated.You can take Book Now!")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    # If Anyone want to add book in the library then this funtion works
    def addBook(self,book):
        self.bookList.append(book)
        print("Book Has been added in booklist")
    # If anyone want to return the book then this function works
    def returnBook(self,book):
        self.lendDict.pop(book)
        print("Book has been returned")
if __name__=='__main__':
    rohit=Library(['Python','C Basics','java','C++ basics','Bootstrap Introduction'],'YadavBook')
    while(True):
        print(f"Welcome to the {rohit.name} library.Enter the choice to continue!")
        print('1.Display Books\n2.Lend a Book\n3.Add a book\n4.Return a book')
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please Enter a valid option!")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            rohit.displayBook()
        elif user_choice==2:
            book=input("Enter the book name that you want to lend:")
            user=input('Enter your name:')
            rohit.lendBook(user,book)
        elif user_choice==3:
            book=input("Enter the book name that you want to add:")
            rohit.addBook(book)
        elif user_choice==4:
            book=input("Enter the book name that you want to return:")
            rohit.returnBook(book)
        else:
            print("Not a valid option!")
        print("press q to quit and c to continue!")
        user_choice2=''
        while(user_choice2!='q' and user_choice2!='c' ):
            user_choice2=input()
            if user_choice2=='q':
                quit()
            elif user_choice2=='c':
                continue
