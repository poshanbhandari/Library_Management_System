#Function to load data

list2=[]

def load():

        
        file= open('books.txt','r')
       
        contents= file.read()

        
        file.close()

        
        list1= contents.split('\n')
        
        
        
        for each_item in list1:
                list2.append(each_item.split(","))
        return list2




def showing_books(source):
    print("Books Id" + "\tBooks name" +"\tBooks Author Name" + "\t\tQuantity"+"\t\tBooks price" +'\n')
    for each in source:
        print(each[0]+'\t'+each[1]+'\t'+each[2]+'\t\t'+each[3]+'\t'+each[4])
    print("\n")
    




