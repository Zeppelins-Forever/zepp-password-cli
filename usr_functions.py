import os.path
from os import path
import linecache
import time
import random
import hashlib
from cryptography.fernet import Fernet


def userLogin():
    while True:
        #check if external file has a password for the manager, if not, prompt for creation.
        #master password and password list are 2 different files.
        if path.exists('masterPass.txt') == False:
            while True:
                PMpass = input("""Create Master Password (type 'x' to exit the program)-->""") 
                if PMpass == "x" or PMpass == "X":
                    print("Now exiting...")
                    time.sleep(1)
                    return "exit"
                PMpass = PMpass.encode('utf-8')
                hashedPMpass = hashlib.sha512(PMpass).hexdigest() #code sample from https://stackoverflow.com/questions/22058048/hashing-a-file-in-python 
                masterPass = open("masterPass.txt", "w+", encoding="utf-8") #hash the password so it is not openly available to anyone who looks at files.
                masterPass.write(hashedPMpass)
                masterPass.close()
                listEncrypt(0)
                return "FirstLogin"
        else:
            attemptsRemain = 4
            while True:
                userGivenPass = input("What's Your Password?-->").encode('utf-8')
                hashedUserGivenPass = hashlib.sha512(userGivenPass).hexdigest() #hash the user-provided password attempt to compare it to the master password, letting the program chck the password without openly revealing it.
                #linecache.getline(file, lineNum) pulls a specific line number from text file. rstrip removes newline from end of line.
                masterPassTXT = linecache.getline("masterPass.txt", 1).rstrip("\n")
                if hashedUserGivenPass != masterPassTXT: 
                    attemptsRemain -= 1
                    if attemptsRemain == 1:#giving user a limited number of attempts before closing down, as well as implementing a delay upon a couple of failures, slowing the number attempts an attacker could make per second.
                        print(attemptsRemain, "attempt remaining.")
                        continue
                    elif attemptsRemain >= 2:
                        print(attemptsRemain, "attempts remaining.")
                        continue
                    elif attemptsRemain == 0:
                        print("Too many attempts! Now exiting...")
                        time.sleep(1)
                        return "exit"
                listEncrypt(3)
                return "ReturnLogin"

def passQuestions(): #prompt user for password generation options. 
    print("What type of password do you want to generate?\n(0) letters only\n(1) numbers only\n(2) symbols only\n(3) letters & numbers\n(4) letters & symbols\n(5) numbers & symbols\n(6) letters, numbers, and symbols\nPress any other key to exit.")
    while True:
        passType = input("-->")
        if passType not in ("0", "1", "2", "3", "4", "5", "6"): #allow for exiting this menu if not chosen intentionally. 
            break
        print("How many characters long do you want the password to be? (enter a number within 1 and 255)")
        while True: #select password length
            passLength = input("-->")
            try:
                passLength = int(passLength)
            except:
                print("Not within parameters, please try again.")
                continue
            if passLength < 1 or passLength > 255:
                print("Not within parameters, please try again.")
                continue
            passwordResult = passgen(passType, passLength)
            return passwordResult
    return "exit"

def passgen(passType, passLength): #password generator
    #possible choices: (0) letters, (1) numbers, (2) symbols, (3) letter & number, (4) letter & symbol, (5) number & symbol, (6) letter & number & symbol
    #these lists are vital for password generation selection, as these datasets are iterated through for generating letters, numbers, or symbols based on particular criteria.
    lettersOnly = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbersOnly = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbolsOnly = ["!", "@", "#", "$", "%", "^", "&", "*"]
    finalList = []
    i = 0            #the following are different selections and options. See the comment above for the full selection description.
    if passType == "0":
        while i < passLength:
            ranVal = random.randint(0, 51)
            charChoice = lettersOnly[ranVal]
            finalList.append(charChoice)
            i += 1
        returnPass = "".join(finalList)
    elif passType == "1":
        while i < passLength:
            ranVal = random.randint(0, 9)
            charChoice = numbersOnly[ranVal]
            finalList.append(charChoice)
            i += 1
        returnPass = "".join(finalList)
    elif passType == "2":
        while i < passLength:
            ranVal = random.randint(0, 7)
            charChoice = symbolsOnly[ranVal]
            finalList.append(charChoice)
            i += 1
        returnPass = "".join(finalList)
    elif passType == "3":
        while i < passLength:
            ranList = random.randint(0, 3)
            if ranList < 3:
                ranVal = random.randint(0, 51)
                charChoice = lettersOnly[ranVal]
                finalList.append(charChoice)
            else:
                ranVal = random.randint(0, 9)
                charChoice = numbersOnly[ranVal]
                finalList.append(charChoice)
            i += 1
        returnPass = "".join(finalList)
    elif passType == "4":
        while i < passLength:
            ranList = random.randint(0, 3)
            if ranList < 3:
                ranVal = random.randint(0, 51)
                charChoice = lettersOnly[ranVal]
                finalList.append(charChoice)
            else:
                ranVal = random.randint(0, 7)
                charChoice = symbolsOnly[ranVal]
                finalList.append(charChoice)
            i += 1
        returnPass = "".join(finalList)
    elif passType == "5":
        while i < passLength:
            ranList = random.randint(0, 1)
            if ranList == 0:
                ranVal = random.randint(0, 9)
                charChoice = numbersOnly[ranVal]
                finalList.append(charChoice)
            else:
                ranVal = random.randint(0, 7)
                charChoice = symbolsOnly[ranVal]
                finalList.append(charChoice)
            i += 1
        returnPass = "".join(finalList)
    else:
        while i < passLength:
            ranList = random.randint(0, 5)
            if ranList < 3:
                ranVal = random.randint(0, 51)
                charChoice = lettersOnly[ranVal]
                finalList.append(charChoice)
            elif ranList == 4:
                ranVal = random.randint(0, 9)
                charChoice = numbersOnly[ranVal]
                finalList.append(charChoice)
            else:
                ranVal = random.randint(0, 7)
                charChoice = symbolsOnly[ranVal]
                finalList.append(charChoice)
            i += 1
        returnPass = "".join(finalList)
    return returnPass

def sortFileContent(input):  #alphabetizes password list (some ideas taken from https://stackoverflow.com/questions/27123125/sorting-a-text-file-alphabetically-python)
    lines = []  #a list is vital here to assist in organizing data, adding all lines of data to the list so it can be sorted and returned.
    with open(input) as inputVar:
        for line in inputVar:
            lines.append(line)
    lines.sort()
    with open(input, 'w') as output:
        for line in lines:
            output.writelines(line)

def listEncrypt(listEncryptor): #code sampled from https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
    if listEncryptor == 0:          #generate key 
        key = Fernet.generate_key()
        with open("filekey.key", "wb") as filekey:
            filekey.write(key)
    elif listEncryptor == 1:                    #encrypt password list
        if path.exists('passwordList.txt') == True: 
            with open("filekey.key", "rb") as filekey:
                key = filekey.read()
            fernet = Fernet(key)
            with open("passwordList.txt", "rb") as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open("passwordList.txt", "wb") as encryptedFile:
                encryptedFile.write(encrypted)
    elif listEncryptor == 2:                #decrypt password list and generate new key
        with open("filekey.key", "rb") as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open("passwordList.txt", "rb") as encryptedFile:
            encrypted = encryptedFile.read()
        decrypted = fernet.decrypt(encrypted)
        with open("passwordList.txt", "wb") as decryptedFile:
            decryptedFile.write(decrypted) 
        key = Fernet.generate_key()
        with open("filekey.key", "wb") as filekey:
            filekey.write(key)
    else:                                   #just decrypts password list
        if path.exists('passwordList.txt') == True: 
            with open("filekey.key", "rb") as filekey:
                key = filekey.read()
            fernet = Fernet(key)
            with open("passwordList.txt", "rb") as encryptedFile:
                encrypted = encryptedFile.read()
            decrypted = fernet.decrypt(encrypted)
            with open("passwordList.txt", "wb") as decryptedFile:
                decryptedFile.write(decrypted) 