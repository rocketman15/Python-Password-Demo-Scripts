encrypted_password = "83 117 98 115 99 114 105 98 101 "
userInput = input("enter a password to unlock the program ")

def encryptPassword(message):
    encryptedString = ""
    for i in message:
        encryptedString += str(ord(i))
        encryptedString += " " 
    return(encryptedString)

def comparePasswords(encryptedUserPassword, correctEncryptedPassword):
    if encryptedUserPassword == correctEncryptedPassword:
        return(1)
        
    else:
        return(0)

def main():
    print("Access Granted. Are you a subscriber?")

encryptedInput = encryptPassword(userInput)
if comparePasswords(encryptedInput, encrypted_password) == 1:
    main()
else:
    print("Nice Try. Subscribe, then try again")