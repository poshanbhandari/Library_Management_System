
#function which gives the facilities to the user to borrow the books:
#frb=[]
def return_books(iD,source):
    lobb=[]
    
    for each in source:
        
        if iD==each[0]:
            
            for each_item in each:
                
                lobb.append(each_item)

            continue_= True
            while continue_==True:
                try:   
                    tdays=int(input("How long do you kept this book  "))
                    fine_days =tdays - 10
                    continue_=False
                    
                    if tdays>10:
                    
                        tfine= fine_days * 0.10*float(each[-1][1:])
                    
                    else:
                    
                        tfine=0

                    lobb.append(tdays)
                
                    lobb.append(round(tfine,2))
                    

                except:
                    print("Invalid number entered please check the number and try again")   
            
            
            
            
            each[3]=str(int(each[3]) +1)
            
            

            
    return lobb






def increasing(r_note):
             file=open("books.txt",'w')
             counter =0
             for each in r_note:
                 if counter ==0:
                     file.write(str(each[0])+','+str(each[1])+','+str(each[2])+ ","+str(each[3]) +","+str(each[4]))
                     counter+=1
                 else:
                     file.write("\n"+str(each[0])+','+str(each[1])+','+str(each[2])+ ","+str(each[3]) +","+str(each[4]))
             file.close()















            
