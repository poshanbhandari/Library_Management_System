
def showing_books(source):
    print("Books Id" + "\t\tBooks name" +"\t\t\tBooks Author Name" + "\t\tQuantity"+"\t\t"+"Books price" +'\n')
    for each in source:
        print(each[0]+'\t\t\t'+each[1]+'\t\t\t'+each[2]+'\t\t\t'+each[3]+'\t\t\t'+each[4])
    print("\n")
    




def menu_showing():
    print("\t\tEnter 1 to view the avaialable books")
    print("\t\tEnter 2 to borrow the books")
    print("\t\tEnter 3 to return the books")
    print("\t\tEnter 4 to exit the system\n\n")
    
