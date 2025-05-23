## Alfie Ford - 120088076
## Cipher Declarations

#Imports
import random
import csv

#Setup alphabet as a global variable so that you dont need to pass into each function
global alphabet
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz"

#AutoRun - this selects the message which is encrypted for the user. It also selects a key for the other functions although this is sometimes overriden
def autorun():
    posmessages = []
    with open("messages.txt","r") as posmessages_file:
        for line in posmessages_file:
            posmessages.append((line.strip()))
    #Debug
    print(posmessages)
    message = random.choice(posmessages)
    print(message)
    return str(message)
#------------------------
#Cipher1 - Caesar Cipher 
#------------------------
def Caesarcipher():
    message = autorun()
    print(message)
    key = 3 
    encmessage = ""
    #Loop over the plaintext message.
    for character in message:
        #Find the position of the character in the alphabet
        pos = alphabet.find(character)
        #Add the key to the position
        newpos = (pos + key) % 26
        #Get the new character
        newchar = alphabet[newpos]
        #Add the character to the encrypted message
        encmessage += newchar
    #Give the encrypted message back to [app.py]
    print(message)
    return encmessage,message
#------------------------------------
#Cipher2 - Moving Key Caesar Cipher
#------------------------------------
# This uses the same idea as cipher1 but adds 1 to the key for every message encoded
# eg. AAAA --> BCDE
def movingkeycipher():
    message = autorun()
    key = 1 #Startkey
    encmessage = ""
    for character in message:
        pos = alphabet.find(character)
        newpos = (pos + key) % 26
        newchar = alphabet[newpos]
        encmessage += newchar
        key += 1 #Adds one to the key as every letter is encrypted
        #print(key) #Debug
    return encmessage, message

#----------------------------
#Cipher3 - SuperEncipherment
#----------------------------
# This cipher uses the skills from the previous ciphers but adds a crib (supplied to the user) to swap the letters after 
# decoding to find the message.
def superencipherment():
    message = autorun()
    #Sets up a dictionary for the crib
    crib = {}
    with open("crib.txt","r") as cribfile:
        data = csv.reader(cribfile)
        for row in data:
            crib[row[0]] = row[1]
    print(crib)
    #Need to find the letter positions for each character
    #pos = []
    letters = []
    for letter in message:
        for chars in range(len(alphabet)):
            if alphabet[chars] == letter:
                #pos.append(chars)
                letters.append(letter)
    #print(f"**{pos}")
    print(f"**{letters}")
    #Need to swap letters for letter in crib
    halfmessage = ""
    for i in range(len(letters)):
        newhalfchar = crib[letters[i]]
        print(newhalfchar)
        halfmessage += newhalfchar
    print(halfmessage)
    encmessage = ""
    key = 1 #Startkey
    for character in halfmessage:
        pos = alphabet.find(character)
        newpos = (pos + key) % 26
        newchar = alphabet[newpos]
        encmessage += newchar
        key += 1 #Adds one to the key as every letter is encrypted
    return encmessage,message
