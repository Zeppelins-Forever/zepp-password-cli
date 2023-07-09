from usr_functions import *


loginResult = userLogin()
if loginResult == "exit":
    exit()
print("Type 'h' or 'help' for help.")
while True: #loop used to ensure that teh program will not end unless user specifies it should via "x".
    userInput = input("What would you like to do?-->")
    if userInput in ("h", "H", "help", "HELP"): #give user list of options
        print("'s' = show password list\n'a' = add a password\n'r' = remove a password\n'g' = generate a password\n'c' = change master password\n'x' = exit the program")
    elif userInput in ("s", "S"): #option for user to show the password list
        fileExist = os.path.isfile("passwordList.txt")
        if fileExist: #checks if password file has been generated, and prints it to the terminal for viewing.
            passwordListFile = open("passwordList.txt", "r", encoding="utf-8")
            fileContents = passwordListFile.read()
            print(fileContents)
            passwordListFile.close()
        else: #if user doesn't have any passwords.
            print("Cannot show password list. You have no saved passwords.")
    elif userInput in ("a", "A"): #option to add a password to the password list
        print("What is the password for? (Enter a website domain name or other relevent identifier, ie. 'passcode.org' or 'Lock combination')")
        passwordID = input("-->")
        print("What is the username? (if no username, leave blank)")
        passwordUN = input("-->")
        print("Would you like to enter a password manually, or generate one?\n'0' = generate\n'1' = manual")
        while True:
            genOrMan = input("-->")
            if genOrMan != "0" and genOrMan != "1":
                print("Not a valid input.")
                continue
            break
        while True:
            if genOrMan == "0": #if user chooses to generate a password, they are taken to a function to do so. 
                passwordPass = passQuestions()
                break
            elif genOrMan == "1": #manual password generation, user enters a password themselves. 
                passwordPass = input("Enter a password-->")
                break
            else:
                print("That's not a valid option.")
                continue
        if passwordPass == "exit":
            continue
        passDict = {"ID": passwordID, "Username": passwordUN, "Password": passwordPass}
        print(passDict)
        with open("passwordList.txt", "a") as passwordList: #witing password to the password list, appending to the end.
            passwordList.write(str(passDict))
            passwordList.write("\n")
        sortFileContent("passwordList.txt") #custom function alphabetizes the password list. 
        passwordList.close()
        
        #used concepts from both of the following sites.
        #https://www.codespeedy.com/sorting-contents-of-a-text-file-using-a-python-program/#:~:text=Method%20for%20sorting%20contents%20of%20a%20text%20file,the%20steps%20until%20the%20end-of-file%20%28EOF%29%20is%20reached.
        #https://www.geeksforgeeks.org/save-a-dictionary-to-a-file/
    elif userInput in ("r", "R"):
        fileExist = os.path.isfile("passwordList.txt") #check if operations can continue by seeing if file exists. 
        if fileExist:
            with open("passwordList.txt") as pList: #the following few lies add numbers to the beginning of each password printed to the terminal to allow the user to select which to remove. 
                listLength = len(pList.readlines())
            pListFile = open("passwordList.txt", "r")
            count = 1
            for i in range(listLength):
                result = pListFile.readline().rstrip("\n")
                print(str(count) + ")", result)
                count += 1
            print("Which password do you want to remove? (enter a number, 'x' to quit)") #numbers allow user to easily select password to be deleted. Selecting the number removes associated password.
            while True:
                usrChoice = input("-->")
                if usrChoice in ("x", "X"):
                    break
                try:
                    usrChoice = int(usrChoice)
                except: 
                    print("Not a valid choice.")
                    continue
                if usrChoice > listLength or usrChoice < 1: #user can't choose anything outside of the list.
                    print("Not a valid choice.")
                    continue
                with open('passwordList.txt', 'r') as fileReader:
                    lines = fileReader.readlines()
                    position = 1
                    with open('passwordList.txt', 'w') as fileWriter:
                        for line in lines:
                            if position != usrChoice:
                                fileWriter.write(line)
                            position += 1
                pListFile.close()
                if os.path.getsize('passwordList.txt') == 0: #if password list file is empty, delete it, since an empty list interferes with other operations. 
                    os.remove("passwordList.txt")
                break
        else:
            print("Cannot remove a password. You have no saved passwords.") #in case password list is empty.
    elif userInput in ("g", "G"): #generate password without adding to password list, links directly to user function.
        generatedPass = passQuestions()
        if generatedPass == None:
            continue
        print(generatedPass)
    elif userInput in ("c", "C"): #runs the user-built function to change the master password. See "userLogin()".
        os.remove("masterPass.txt")
        loginResult1 = userLogin()
        if loginResult1 == "exit":
            exit()
    elif userInput in ("x", "X"): #exits the program, calls the function to appropriately encrypt data, such as the password list.
        listEncrypt(1)
        print("Now Exiting...")
        time.sleep(1)
        exit()
    else:
        print("That's not a valid input") #handles input outside of the expected range.
    continue
