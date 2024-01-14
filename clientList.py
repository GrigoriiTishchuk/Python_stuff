import random

def Clientregister():

    clientList = []
    while len(clientList) <= 22:
        clientName = input("Enter name: ")
        if clientName =='':
            break
        clientList.append(clientName)
        #target #function #from
    print("Reservations: ", clientList)
    print("Clientell: ", len(clientList))

    return clientList


def ClientTable(clientList):

    clientTableNumber = []
    tableList = []
    
    for i in range(1, 25, 1):
        tableList.append(i)

    clientTableNumber = random.sample(tableList, len(clientList))

    print("Reserved Tables:", clientTableNumber)

    return clientList, clientTableNumber

def ClientListing():
    clientList, clientTableNumber = ClientTable(Clientregister())
    x = int(0)
    for i in range(len(clientList)):
        clientAndTable = str(clientList[x]) + '\t'  + "----------" + '\t' + "Table: " + str(clientTableNumber[x])
        x += 1
        print(clientAndTable)



def main():
    client = ClientListing()

if __name__ == "__main__":
    main()