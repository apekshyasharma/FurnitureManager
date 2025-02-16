import read
import datetime

def writeFile():
    """Writing updated data to the furniture.txt text file."""
    furniture_file=open("furniture.txt","w")
    for line in read.listLine:
        furniture_file.write(','.join(line))
    furniture_file.close()

def validateQuantity(productId,qty): 
    """checks whether the desired product quantity is available at the stock or not."""
    listLine=read.listLine
    print(int(listLine[productId-1][3]))
    return (int(listLine[productId-1][3])>=qty and qty>0 ) #int converts the string value in listline quantity.

def validateproductid(id):
    """checks whether the desired product Id exists or not."""
    listLine = read.listLine
    if len(listLine) >= id and id>0 :
        return True
    else:
        return False

def selldone(id,quantity):
    """updates the inventory and sets quantity"""
    listline=read.listLine
    try:
        temp = int(listline[id - 1][3])
        print(temp)
        temp -= quantity
        print(temp)
        read.listLine[id - 1][3]=str(temp)
        writeFile()
    except:
        print("Cannot update the value")


