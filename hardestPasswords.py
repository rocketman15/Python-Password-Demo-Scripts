import hashlib
passwordHash = "5f4dcc3b5aa765d61d8327deb882cf99" # password = password
userInput = input("enter the password to access the program ")

def hashInput(input):
    result = hashlib.md5(input.encode())
    return(result.hexdigest())


def comparePasswords(userInput, correctPassword):
    if userInput == correctPassword:
        return(1)
    else:
        return(0)

def main():
    print("Access Granted. Have you left a comment yet?")

hashedPassword = hashInput(userInput)
if comparePasswords(hashedPassword, passwordHash) == 1:
    main()
else:
    print("Nice try. leave a comment then try again.")