import showing
import returns
import load_data
import Note_generator as N

import borrow




b_note=[]
list4=load_data.load()
reutrned_note=[]
print("\n")
print("*******************************Welcome TO Library Management System******************************")
print("\n")

user =input("[*] Dear user Enter your name: ")
            
    
flow=True
while flow == True:
    print('\n')
    showing.menu_showing()
    wish =input("[*] Dear" " "+ user +" "+"select any option that you want to do:\n ")
    

    if wish=="1":
        
        print('\n')
        showing.showing_books(list4)
        

        
    elif wish =="2":
        
        ID=input("[*] Enter the Id of the book that you want to borrow: ")
        b_note=borrow.Borrowing_books(ID,list4)
        


        
        
    elif wish=="3":
        captured_data =[]
        
        ID =input("[*] Enter the book id that you want to return back the library")
        print("\n")
       
        
        captured_data=returns.return_books(ID,list4)
               
        
        if len(captured_data)>0:
            #print("\n")
            print("[*] Thank you for returning the book")
            reutrned_note.append(captured_data)

            
        else:
            
            print("[!] Sorry there is no such book with this ID")

        print(captured_data)
        
        


         
        
    elif wish=="4":
        
        N.borrower_note(user,b_note)
        N.return_note(user,reutrned_note)
        returns.increasing(list4)
        
        exit()

      
        
    else:
        print("invalid choice")
    
    
