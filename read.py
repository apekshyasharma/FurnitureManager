listLine=[] #Global variable list so all function can use it for file handeling.
   
def readFile():
    """Accessing the furniture data from the text file."""
    furniture_file=open("furniture.txt","r")
    for line in furniture_file:
        listLine.append(line.split(","))
    furniture_file.close()
    return listLine 

def costumerDet():
    """Checking whether the user input is empty or not. """
    print("%"*100)
    print(" "*30+"WELCOME TO THE CUSTUMER DETAIL FORM ")
    print("%"*100 +"\n")
    while True:
        costumerName=input("Please enter the costumer's name:\n ")
        if(costumerName == ""):
            print("Name cannot be empty, Please try again :( \n")
        else:
            break
    while True:
        costumerPhoneNum=input("Please enter costumer's contact details:\n")
        if(costumerPhoneNum==""):
            print("Contact details cannot be empty.Please try again :( ")
        else:
            break
    while True:
        costumerAddress=input("Please enter constumer's adress:\n ")
        if(costumerAddress==""):
            print("Address details cannot be empty. Please try again :( ")
        else:
            break
    return costumerName,costumerPhoneNum,costumerAddress


        

