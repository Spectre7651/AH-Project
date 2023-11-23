## Alfie Ford - 120088076
## Cipher Declarations

#Imports
import random

#Global Vars
alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
#AutoRun (gen messages and keys)

def autorun():
    posmessages = []
    with open("possmessages.txt","r") as posmessages_file:
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

    

#debug

print(caesarcipher(alphabet))