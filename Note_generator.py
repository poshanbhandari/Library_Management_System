def borrower_note(name,note):
    file=open("borrower_note.txt","w")
    
    file.write("Borrower Name:-\t"+name+"\t" "\n")
    file.write("\n")
    total =0
    file.write("Book ID" +"\tBook Name" +"\tBook Author"  +"\t Price\n")
    for each in note:
        
        file.write(each[0]+'\t' +each[1]+"\t"+each[2]+"\t"+each[4]+'\n')
        price=each[4][1:]
        total+=float(price)
        
    file.write("*******************************************************")
    file.write("\n")
    file.write("the total price is\t\t\t\t"+"$"+str(total))
    file.close

def return_note(name,r_note):
    file=open("return_note.txt",'w')
    file.write("Borrower Return Name:-\t " +name+"\n")
    file.write("\n")
    
    file.write("Returned Book Id \t Borrowed price\t Borrowed days \tfine\n")
    file.write("----------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    
    file.write("\n")
    total=0
    for each in r_note:
        
        file.write(str(each[0])+'\t\t' + str(each[4] )+"\t\t"+str(each[5])+'\t\t'+"$"+str(each[6])+"\n")
        
        price=float(each[4][1:]) + float(each[6])
        
        total+=price
        
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------------------\n")
    file.write("The total price is ----------\t\t\t"+"$"+str(total))
    file.close()
