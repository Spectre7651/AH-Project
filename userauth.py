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
            authunames.append(row[0])
            authunames.append(row[1])
            accountname.append(row[2])
    #Check if the user details supplied is correct
    for i in range(len(authunames)):
        if uname == authunames[i] and passwd == authpasswds[i]:
            return "AUTHORISED",accountname[i]
            break
        elif uname == authunames[i] and passwd != authpasswds[i]:
            return "INC-PASSWD"
        elif uname != authunames[i] and passwd == authpasswds[i]:
            return "INC-UNAME"
        else:
            #Return User Not Found (UNF)
            return "UNF"
        

