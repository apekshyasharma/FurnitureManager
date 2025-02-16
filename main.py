'''
Importing  all the python files (read,operation,write) to the main file.
'''
from read import *
from operation import *
from write import *
#read .txt inventory from read.py module. #listData is 2d list.
listData = readFile()

#Code for the user input.
print(">"*45+" MOST WELCOME TO THE BRJ FURNITURE STORE "+"<"*45)
while True: #This is the main loop.

    finalList=[]
    print("\nEnter buy to purchase.")
    print("Enter sell to vend.")
    print("Enter exit to leave.")
    question=input("\n Please enter the suitable option according to your preferences:\n ")

#Performing different tasks according to the nature of transaction.
    if (question.upper()=="SELL"):
        while True: #loop for selling items to the customer by user.
            purchaselist=[] #empty list for appending datas of item to be purchased by the customer.

            listTable(listData) #invoking listTable() function from operation.py module. Passing 2d list as parameter.
            while True:                 #loop for validating product Id and quantity.

                try:        #Exceptional Handling for incorrect input format.
                    idValue=int(input("Please enter the ID of product you want to purchase :)\n"))
                    check =validateproductid(idValue)       #checks whether the product id input is in the inventory.(input type is boolean)
                    if not check :          #if check is false it will ask again.
                        continue
                    else:
                        break       #if check is true it will continue the program/exit the loop.

                except:             #when data is not an integer exception will take place.
                    print("Please try entering valid input format according to the inventory product table :( ")

            while True:
                try: #exception handling for the product quantity.
                    quantityValue=int(input("Please enter the quantity of item you want to purchase :)\n "))
                    check = validateQuantity(idValue,quantityValue)#checks the asked quantity is in inventory or not
                    if not check : #if check is false it will ask again
                        continue
                    else:
                        selldone(idValue, quantityValue) #update the quantity to the inventory .txt and 2d list both

                        listLine = read.listLine # read the 2D list of inventory data
                        # append data of current product id datas such as id, company name, item name, quantity and price to purchase list
                        purchaselist.append(idValue)
                        purchaselist.append(listLine[idValue - 1][1])
                        purchaselist.append(listLine[idValue - 1][2])
                        purchaselist.append(quantityValue)
                        purchaselist.append(listLine[idValue - 1][4])
                        #the data of current purchase is than appended to the final list which is appended till all purchase item is not done
                        finalList.append(purchaselist)
                        break
                except:
                    # exception handling for invalid quantity
                    print("Please enter the valid quantity")



            #asks the user if the purchase items are all done or wants to add items again
            queryYn=input("Would you like to order more items from us?\n Press y to continue.\n press anyother key to create invoice.\n")
            #if only input is true it will ask again else it will proceed to invoice generation
            if (queryYn.upper() !="Y"):
                data =costumerDet() #this function will pass a tuple by asking the data from the user about their details
                invoice(data,finalList) #this function will take details of the user and the list of items that is purchased to generate the invoice
                break


    elif (question.upper()=="BUY"):
                while True:
                    purchaselist = []
                    listTable(listData)
                    while True:

                        try:  # Exceptional Handling for incorrect input format.
                            idValue = int(input("Please enter the ID of product you want to purchase :)\n"))
                            check = validateproductid(idValue)
                            if not check:  # if check is false it will ask again.
                                continue
                            else:
                                break  # if check is true it will continue the program/exit the loop.
                        except:
                            print("Please try entering valid input format according to the product table :( ")

                    while True:
                        try:  # exceptional handling for the product quantity.
                            quantityValue = int(input("Please enter the quantity of item you want to purchase :)\n "))
                            if quantityValue <= 0:
                                continue
                            selldone(idValue, -quantityValue)
                            listLine = read.listLine
                            purchaselist.append(idValue)
                            purchaselist.append(listLine[idValue - 1][1])
                            purchaselist.append(listLine[idValue - 1][2])
                            purchaselist.append(quantityValue)
                            purchaselist.append(listLine[idValue - 1][4])
                            finalList.append(purchaselist)
                            break
                        except:
                            print("error upadating value")
                    queryYn = input(
                        "Would you like to order more items from us?\n Press y to continue.\n press anyother key to create invoice.\n")
                    if queryYn.upper() != "Y":
                        buy(finalList)
                        break
                    else:
                        continue




    elif (question.upper()=="EXIT"):
        print("exit")
        exit(0)
    else:
        print("Invalid Input.\nPlease try again with valid input.\n")


