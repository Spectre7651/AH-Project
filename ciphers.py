## Alfie Ford - 120088076
## Cipher Declarations

#Imports
import random
import csv

#Global Vars
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#AutoRun (gen messages)

def autorun():
    posmessages = []
    with open("messages.txt","r") as posmessages_file:
        for line in posmessages_file:
            posmessages.append((line.strip()).upper())
    print(posmessages) #Debug
    message = random.choice(posmessages)
    print(message)
    key = random.randint(1,26)
    print(key) # Debug
    return message,key
#Caesar Cipher
def caesarcipher(alphabet):
    message,key = autorun()
    encmessage = ""
    for character in message:
        pos = alphabet.find(character)
        newpos = (pos + key) % 26
        newchar = alphabet[newpos]
        encmessage += newchar
    return encmessage

#Moving Key Caesar Cipher
def movingkeycipher(alphabet):
    message,key = autorun()
    key = 1 #Startkey
    encmessage = ""
    for character in message:
        pos = alphabet.find(character)
        newpos = (pos + key) % 26
        newchar = alphabet[newpos]
        encmessage += newchar
        key += 1 #Adds one to the key as every letter is encrypted
        print(key) #Debug
    return encmessage
        
def supercipherment(alphabet):
    message,key = autorun()
    crib = {}
    with open("crib.txt","r") as cribfile:
        data = csv.reader(cribfile)
        for row in data:
            crib[int(row[0])] = int(row[1])
    print(crib)
    #Need to find the letter positions for each character
    pos = []
    letters = []
    for letter in message:
        for chars in range(len(alphabet)):
            if alphabet[chars] == letter:
                pos.append(chars+1)
                letters.append(letter)
    print(pos)
    print(letters)
    #Need to swap letters for letter in crib (bin search)
    halfmessage = ""
    for i in range(len(message)):
        oldpos = int(pos[i])
        newpos = crib[oldpos]
        print(newpos)
        halfmessage += alphabet[newpos-1]
    print(halfmessage)

#debug

print(caesarcipher(alphabet))
print(movingkeycipher(alphabet))
supercipherment(alphabet)