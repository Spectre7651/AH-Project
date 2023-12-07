import csv

#Checks User Details for login
def checkuserdetails(uname,passwd):
    #Setup
    authunames = []
    authpasswds = []
    accountname = []
    #Open and Read the user details file
    with open("userdetails.txt","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            authunames.append(row[1])
            authpasswds.append(row[2])
            accountname.append(row[3])
            #print(authunames,authpasswds,accountname)
    
    #Check if the user details supplied is correct
    for i in range(len(authunames)):
        if uname == authunames[i] and passwd == authpasswds[i]:
            return "AUTHORISED",accountname[i]
            break
        elif uname == authunames[i] and passwd != authpasswds[i]:
            return "INC-PASSWD"," "
        else:
            #Return User Not Found (UNF)
            return "UNF"," "

#checkuserdetails("admin","admin")


def leaderboard():
    #Setup 2D array, so that a whole user record can be moved easily during the sort
    #Data will follow useracct = [[id,name,points],[...]]
    useracct = []

    #Open and Read the user details file
    with open("userdetails.txt","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            useracct.append([int(row[0]),row[3],int(row[4])])
    #Debug
    print(useracct)

    #Perform a bubble sort to find user with the highest point score
    def bubble_sort(useracct):
        array = useracct
        n = len(array)
        swapped = True
        while swapped == True and n >= 0:
            for i in range(n-1): #Loop over the array
                if int(array[i][2]) < int(array[i+1][2]): #If this value is smaller than the next one..
                    #Swap records in the array
                    temp = array[i]
                    print(temp)
                    array[i] = array[i+1]
                    array[i+1] = temp
                    swapped = True
            n = n-1
        return array #Return the sorted array
    useracct_sorted = bubble_sort(useracct)
    print(useracct_sorted)

