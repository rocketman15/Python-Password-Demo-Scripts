import hashlib # import the hashlib library. 
passwordHash = "5f4dcc3b5aa765d61d8327deb882cf99" # this is the password hash. the default password is "password", but you can change it if you like. make sure that there are no spaces. 
userInput = input("enter the password to access the program ")# get user input

def hashInput(input): # this function will hash a string. 
    result = hashlib.md5(input.encode())
    return(result.hexdigest())


def comparePasswords(userInput, correctPassword):# this function will compare two values; if they are equal, it will return a value of 1. if not, a value of zero. 
    if userInput == correctPassword:
        return(1)
    else:
        return(0)

def main():# put the code that you want to run after a successful unlock here. 
    print("Access Granted. Have you left a comment yet?")

hashedPassword = hashInput(userInput)
if comparePasswords(hashedPassword, passwordHash) == 1:
    main()
else:# put the code you want to run after a failed unlock here. 
    print("Nice try. leave a comment then try again.")
