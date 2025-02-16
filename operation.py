from read import *
import datetime
from read import readFile

def listTable(data):
    """Displaying the 2d list in the form of a table."""
    print("="*115)
    print("="*115)
    print("ID"+" "*6+"Manufacturer Name"+" "*15+"Product Name"+" "*13+"Product Quantity"+" "*15+"Pricing details")
    print("="*115)
    for idx in range(len(data)):
        print(data[idx][0]+" "*(8-len(data[idx][0]))+data[idx][1]+" "*(32-len(data[idx][1]))+data[idx][2]+" "*(25-len(data[idx][2]))+data[idx][3]+" "*(31-len(data[idx][3]))+data[idx][4]+" "*(15-len(data[idx][2])))
    print("="*120)
    print("="*120)

def invoice(data,items):
    """this function will create invoice for the items sold by the brj furnuture to the costumers"""
    invoicenum ="BRJ-SELL-"+ str(datetime.datetime.now().strftime('%H%M%S'))
    invoice =(
        "///////////////////////////////////////////////////////////////////////////////////////////\n"+
        "                                    BRJ FURNITURE\n"+
        "///////////////////////////////////////////////////////////////////////////////////////////\n"+
        #the below line takes details of the costumer as data with type list and adds the date and time of purchase
        "invoice Number    : "+ invoicenum +"\n" 
        "date and time     : " +datetime.datetime.now().strftime('%Y-%m-%d')+ " : "+ datetime.datetime.now().strftime('%H:%M:%S')+"\n"
        "Customer Name     : "+ data[0]+"\n"
        "Customer Address  : " + data[2]+"\n"
        "Customer Phone Num: " + data[1]+"\n"
        "///////////////////////////////////////////////////////////////////////////////////////////\n"+
        " ID      Company                         Item                     quantity        price \n"
    )
    #this below loop will go through the list of purchase in the items 2d list and add the data as string to the invoice string
    for i in range(len(items)):

        invoice += (" "+str(items[i][0])+ "      "+str(items[i][1])+ "    "+str(items[i][2])+ "            "+str(items[i][3])+ "            "+str(items[i][4])+ "\n")

    invoice +=(
        "///////////////////////////////////////////////////////////////////////////////////////////\n"

    )
    subTotal = 0
    shipping = 10 # shipping is set as $10
    #this loop will go through each purchase list calculate subtotal
    for i in range(len(items)):
        price = int(items[i][4].replace("$", ""))# the $ sign is removed for the price and set as integer
        subTotal+= int(items[i][3]*price) # price is calculate with quantity and price and added to the subtotal till the list is all done
        #the final price data are added to invoice string inclulding shipping, vat amount and total with val as total amount
    invoice +=(
        "Subtotal     : "+ str(subTotal)+ "\n" +
        "Shipping     : "+ str(shipping)+ "\n"+
        "Vat amount   : "+ str(subTotal*0.13)+ "\n"+
        "Total amount : " + str(subTotal+subTotal*0.13 + shipping)

    )
    print(invoice)
    invoicename = invoicenum
    # Write the invoice to a .txt file
    with open(invoicename, "w") as file:
        file.write(invoice)
    file.close()

def buy(items):
    """this function will print bill for items bought by the brj furnuture """
    #for buying the details is of the Brj furniture which is all known only the purchased data is inputed 
    invoicenum = "BRJ-BUY-" + str(datetime.datetime.now().strftime('%H%M%S'))
    invoice = (
            "///////////////////////////////////////////////////////////////////////////////////////////\n" +
            "                                    BUYING INVOICE\n" +
            "///////////////////////////////////////////////////////////////////////////////////////////\n" +
            "invoice Number    : " + invoicenum + "\n"
            "date and time     : " + datetime.datetime.now().strftime('%Y-%m-%d') + " : " + datetime.datetime.now().strftime('%H:%M:%S') + "\n"
            "Customer Name     : " + "BRJ FURNITURE" + "\n"
            "Customer Address  :" + "Kamalpokhari, Kathmandu" "\n"
            "Customer Phone Num:" + "0987654322" + "\n"
            "///////////////////////////////////////////////////////////////////////////////////////////\n" +
            " ID      Company                         Item                     quantity        price \n"
    )
    #this below loop will go through the list of purchase in the items 2d list and add the data as string to the invoice string
    for i in range(len(items)):
        invoice += (" " + str(items[i][0]) + "      " + str(items[i][1]) + "    " + str(
            items[i][2]) + "            " + str(items[i][3]) + "            " + str(items[i][4]) + "\n")

    invoice += (
        "///////////////////////////////////////////////////////////////////////////////////////////\n"

    )
    subtotal = 0
    shipping = 10# shipping is set as $10
    #this loop will go through each purchase list calculate subtotal
    for i in range(len(items)):
        price = int(items[i][4].replace("$", ""))# the $ sign is removed for the price and set as integer
        subtotal+= int(items[i][3]*price) # price is calculate with quantity and price and added to the subtotal till the list is all done
        #the final price data are added to invoice string inclulding shipping, vat amount and total with val as total amount

    invoice += (
            "Subtotal     : " + str(subtotal) + "\n" +
            "Shipping     : " + str(shipping) + "\n" +
            "Vat amount   : " + str(subtotal * 0.13) + "\n" +
            "Total amount : " + str(subtotal + subtotal * 0.13 + shipping)

    )
    print(invoice)
    invoicename = invoicenum
    # Write the invoice to a .txt file
    with open(invoicename, "w") as file:
        file.write(invoice)
    file.close()
