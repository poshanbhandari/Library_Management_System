selected_book =[]

def Borrowing_books(Id,twoD):
    
    for each_item in twoD:
        if Id ==each_item[0]:
            if int(each_item[3])>0:
                 print("you have sucessfully borrowed")
                 a=int(each_item[3])-1
                 each_item[3]=str(a)
                 selected_book.append(each_item)
                 print(selected_book)
                 
            else:
                print("All the books with this ID has already been borrowed .Please try again later..")
            break;

    else:
        print("No such books available at this moment")
    return selected_book


 
