encrypted_password = "83 117 98 115 99 114 105 98 101 "# this is the ascii value for the password. make sure to put a single space between values, 
#and that there are no extra spaces, except a single space at the end
userInput = input("enter a password to unlock the program ")#get user input

def encryptPassword(message):#this function will encrypt the password
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

def main():# put the code that you want to run after a successful unlock here. 
    print("Access Granted. Are you a subscriber?")

encryptedInput = encryptPassword(userInput)
if comparePasswords(encryptedInput, encrypted_password) == 1:
    main()
else:# put the code that you want to run after a failed unlock here. 
    print("Nice Try. Subscribe, then try again")
