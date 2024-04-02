# Alfie Ford - 120088076

#This Script is everything to do with the user management of the project

#It Includes functions/procedures for:
    #Importing user data from csv
    #Checking user details
    #Updating points values in the webapp
    #Computing the leaderboard
    #Updating the users points in the csv file


#General Imports
import csv

#This is run by the functions in this file that need the data from the userdetails.csv file
def importuserdata():
    #Setup 2d array for userdetails
    #Layout of array:
    #         [[usernames][passwords][accountnames][accountpoints]]
    authuser_details = [[],[],[],[]]
    #Open and Read the user details file
    with open("userdetails.csv","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            #This transplants the csv data into the 2d array
            authuser_details[0].append(row[0])
            authuser_details[1].append(row[1])
            authuser_details[2].append(row[2])
            authuser_details[3].append(row[3])
    #Debug
    for i in authuser_details:
        print(i)
    #Give the 2d array back to the function that called this function
    return authuser_details


#This Checks User Details for login.
#This is called from app.py when the form on index.html is submitted to auth a user.
def checkuserdetails(uname,passwd):
    #Setup (get the data from userdetails.csv)
    authuser_details = importuserdata()
    unf = False #This is the user not found flag
    #Check if the user details supplied is correct
    for i in range(len(authuser_details[0])):
        #If the username and password matches an account:
        print(authuser_details[0][i],authuser_details[1][i])
        if uname == authuser_details[0][i] and passwd == authuser_details[1][i]:
            return "AUTHORISED",authuser_details[2][i],authuser_details[3][i],authuser_details[0][i] #Send the ok and accountname points and username to the app.py program
            unf = False
            break #Dont bother to loop anymore

            #If the username belongs to an account but the password is incorrect:
        elif uname == authuser_details[0][i] and passwd != authuser_details[1][i]:
            return "INC-PASSWD"," "," "," " #Tell the app.py script to ask the user to try again
            unf = False
            break
            #If the username doesn't belong to an account:
        else:
            unf = True
    if unf == True:
        return "UNF"," "," "," " #Return user not found and get the app to tell the user.
    else:
        pass


#This grabs the users new points after a challenge is completed
def getpoints(accountuname):
    #Setup
    authuser_details = importuserdata()
    #Find the username needed and pass back the points to the main program.
    for i in range(len(authuser_details[0])):
        if accountuname == authuser_details[0][i]:
            return authuser_details[3][i]
        else:
            pass

#This calculates the leaderboard and shows where the current user is in the table (called from launchpad.html)
def leaderboard(currentuser):
    #Setup 2D array, so that a whole user record can be moved easily during the sort
    #Data will follow useracct = [[accntname,points],[...]]

    #Setup the useracct array which is in a different format to easily move the records about the array while sorting
    useracct = []
    #Open and Read the user details file
    with open("userdetails.csv","r") as userdetails_file:
        data = csv.reader(userdetails_file)
        for row in data:
            useracct.append([row[0],int(row[3])])
    #Please note that the [with open] method automatically closes the file :)
    #Debug
    print(useracct)
    print(currentuser)

    #Perform a bubble sort to find user with the highest point score
    def bubble_sort(useracct):
        n = len(useracct)
        swapped = True
        while swapped == True and n >= 0:
            for i in range(n-1): #Loop over the array
                if int(useracct[i][1]) < int(useracct[i+1][1]): #If this accounts point score is smaller than the next one..
                    #Swap records in the array (this swaps the whole account sub-array inn the useracct array)
                    temp = useracct[i]
                    #print(temp)
                    useracct[i] = useracct[i+1]
                    useracct[i+1] = temp
                    swapped = True
            n = n-1
        return useracct #Return the sorted useracct array with the most user with the most points at the start of the array.
    useracct_sorted = bubble_sort(useracct)
    print(useracct_sorted)    #position = 0
    for i in range(len(useracct_sorted)):
        if str(useracct_sorted[i][0]) == str(currentuser):
            pointsbehind = useracct_sorted[0][1] - useracct_sorted[i][1]
            if i == 0:
                position = f"Congratulations You Are Number {i+1} On The Leaderboard!"
            else:
                position = f"You Are Number {i+1} On The Leaderboard. Only {pointsbehind} Points Behind The Leader {useracct_sorted[0][0]}"
            return position
#DEBUG leaderboard("test")

#This saves the new point score of the user to the userdetails.csv file
def addpoints(targetaccountname,points):
    #Setup
    authuser_details = importuserdata()
    #Search for the target username in the accounts
    for i in range(len(authuser_details[0])):
        if authuser_details[0][i] == targetaccountname:
            #Ammend the accounts point values
            authuser_details[3][i] = str(int(authuser_details[3][i])+ points)
            #Re-write the data to the csv file
            with open("userdetails.csv","w") as userdetails_file:
                for i in range(len(authuser_details[0])):
                    userdetails_file.write(f"{authuser_details[0][i]},{authuser_details[1][i]},{authuser_details[2][i]},{authuser_details[3][i]}\n")
        else:
            pass
