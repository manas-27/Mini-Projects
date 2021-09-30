import datetime


print("**********Enter name of books in block letters**************")
novels=['BRAVE NEW WORLD','DARKNESS AT NOON','INVISIBLE MAN','TO THE LIGHTHOUSE','NATIVE SON']
story_bks=['SHADOW AND BONE','SIX OF CROWS','THE YOUNG ELITES','MASK OF SHADOWS','MY TORIN']
entrance=['H C VERMA','R D SHARMA','D C PANDEY','BIOLOGY','CHEMISTRY 1','CHEMISTRY 2']
name=[]
lend_bks=[]




def add_book():
    while True:
        print("Which type of book you want to add: ")
        print("1. A Novel")
        print("2. A Story Book")
        print("3. A Book related to Entrance Exam")
        print("4. Exit")
        a=int(input())
        if a==1:
            b=input("Enter the name of the book you want to add: ")
            novels.append(b)
        elif a==2:
            b=input("Enter the name of the book you want to add: ")
            
            story_bks.append(b)
        elif a==3:
            b=input("Enter the name of the book you want to add: ")
            
            entrance.append(b)
        elif a==4:
            print("****************************************************")
            break
        else:
            print("*****************Enter proper choice*************************")
            




def display_book():
    while True:
        print("Which type of book you want to Display: ")
        print("1. A Novel")
        print("2. A Story Book")
        print("3. A Book related to Entrance Exam")
        print("4. Exit")
        a=int(input())
        if a==1:
            print("Novels: \n")
            for i in novels:
                print(i)
            print("****************************************************")
        elif a==2:
            print("Story books: \n")
            for i in story_bks:
                print(i)
            print("****************************************************")
        elif a==3:
            print("Entrance Books: \n")
            for i in entrance:
                print(i)
            print("****************************************************")
        elif a==4:
            print("****************************************************")
            break
        else:
            print("*****************Enter proper choice*************************")
            



def ret_book():
    n=input("Enter your name: ")
    n.upper()
    r=input("Enter the name of book to be returned: ")
    r.upper
    name.remove(n)
    lend_bks.remove(r)
    print("Date and Time you returned the book: ",datetime.datetime.now())
    print("****************************************************")



def lend_book():
    print("Which type of book you want to Display: ")
    print("1. A Novel")
    print("2. A Story Book")
    print("3. A Book related to Entrance Exam")
    a=int(input())
    if a==1:
        n=input("Enter your Name: ")
        
        l=input("Enter name of the book you want to lend: ")
        
        if l not in  novels:
            print("Book is not available in the library")
        elif l not in lend_bks:
            lend_bks.append(l)
            name.append(n)
            print("Date and Time you borrowed the book: ",datetime.datetime.now())
        else:
            print("Book is used by someone else !!!")
        print("****************************************************")
    elif a==2:
        n=input("Enter your Name: ")
        
        l=input("Enter name of the book you want to lend: ")
        
        if l not in  story_bks:
            print("Book is not available in the library")
        elif l not in lend_bks:
            lend_bks.append(l)
            name.append(n)
            print("Date and Time you borrowed the book: ",datetime.datetime.now())
        else:
            print("Book is used by someone else !!!")
        print("****************************************************")
    else:
        n=input("Enter your Name: ")
        
        l=input("Enter name of the book you want to lend: ")
    
        if l not in  entrance:
            print("Book is not available in the library")
        elif l not in lend_bks:
            lend_bks.append(l)
            name.append(n)
            print("Date and Time you borrowed the book: ",datetime.datetime.now())
        else:
            print("Book is used by someone else !!!")
        print("****************************************************")


while True:
    print("Enter your choice: ")
    print("1.Display Books")
    print("2.Add Book")
    print("3.Lend Book")
    print("4.Return Book")
    print("5.Exit")
    print("-------------------------------------------------------")
    a=int(input())
    print("-------------------------------------------------------")
    if a==1:
        display_book()
    elif a==2:
        add_book()
    elif a==3:
        lend_book()
    elif a==4:
        ret_book()
    elif a==5:
        print("****************************************************")
        break
    else:
        print("Enter proper Choice")
        print("****************************************************")

