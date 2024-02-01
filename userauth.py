# Alfie Ford - 120088076

#This is the script that holds the code for:
#   The login authentication
#   The leaderboard compute
#   Point system

#Imports
import csv

#Checks User Details for login.
#This is called from app.py when the form on index.html is submitted to auth a user.
def checkuserdetails(uname,passwd):
    #Setup
    authunames = []
    authpasswds = []
    accountname = []
    accntpoints = []
    #Open and Read the user details file
    with open("userdetails.csv","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            authunames.append(row[0])
            authpasswds.append(row[1])
            accountname.append(row[2])
            accntpoints.append(row[3])
            #print(authunames,authpasswds,accountname)
    incpasswd = False
    #Check if the user details supplied is correct
    for i in range(len(authunames)):
        #If the username and password matches an account:
        if uname == authunames[i] and passwd == authpasswds[i]:
            return "AUTHORISED",accountname[i],accntpoints[i],authunames[i] #Send the ok and accountname to the app.py program
            break #Dont bother to loop anymore
          #If the username belongs to an account but the password is incorrect:
        elif uname == authunames[i] and passwd != authpasswds[i]:
            incpasswd = True
        #If the username doesn't belong to an account:
        else:
            pass
    #If the username belongs to an account but the password is incorrect:
    if incpasswd == True:
        return "INC-PASSWD"," "," " #Tell the app.py script to ask the user to try again
    #If the username doesn't belong to an account:
    else:
        return "UNF"," "," " #Return user not found and get the app to tell the user.

#checkuserdetails("admin","admin")

#This grabs the current points after a challange is completed
def getpoints(accountuname):
    #Setup
    authunames = []
    authpasswds = []
    accountname = []
    accntpoints = []
    #Open and Read the user details file
    with open("userdetails.csv","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            authunames.append(row[0])
            authpasswds.append(row[1])
            accountname.append(row[2])
            accntpoints.append(row[3])
    #Find the username needed and pass back the points to the main program.
    for i in range(len(authunames)):
        if accountuname == authunames[i]:
            return accntpoints[i]
        else:
            pass
#This calculate the leaderboard and shows where the current user is in the table (called from launchpad.html)

def leaderboard():
    #Setup 2D array, so that a whole user record can be moved easily during the sort
    #Data will follow useracct = [[id,name,points],[...]]

    #Setup the useracct array
    useracct = []
    #Open and Read the user details file
    with open("userdetails.txt","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            useracct.append([int(row[0]),row[3],int(row[4])])
    #Please note that the [with open] method automatically closes the file :)
    #Debug
    print(useracct)

    #Perform a bubble sort to find user with the highest point score
    def bubble_sort(useracct):
        array = useracct
        n = len(array)
        swapped = True
        while swapped == True and n >= 0:
            for i in range(n-1): #Loop over the array
                if int(array[i][2]) < int(array[i+1][2]): #If this accounts point score is smaller than the next one..
                    #Swap records in the array (this swaps the whole account sub-array inn the useracct array)
                    temp = array[i]
                    #print(temp)
                    array[i] = array[i+1]
                    array[i+1] = temp
                    swapped = True
            n = n-1
        return array #Return the sorted useracct array with the most user with the most points at the start of the array.
    useracct_sorted = bubble_sort(useracct)
    print(useracct_sorted)

#This saves the new point score of the user to the userdetails.csv file
def addpoints(targetaccountname,points):
    #Setup
    authunames = []
    authpasswds = []
    accountname = []
    accntpoints = []
    #Open and Read the user details file
    with open("userdetails.csv","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            authunames.append(row[0])
            authpasswds.append(row[1])
            accountname.append(row[2])
            accntpoints.append(row[3])
            #print(authunames,authpasswds,accountname)
    #Search for the username in the accounts
    for i in range(len(authunames)):
        if authunames[i] == targetaccountname:
            #Ammend the accounts point values
            accntpoints[i] = str(int(accntpoints[i])+ points)
            #Re-write the data to the csv file
            with open("userdetails.csv","w") as userdetails_file:
                for i in range(len(authunames)):
                    userdetails_file.write(f"{authunames[i]},{authpasswds[i]},{accountname[i]},{accntpoints[i]}\n")
        else:
            pass
