input = input("enter a string to convert to ascii")# get user input 

def encrypt(message):# this function will encrypt the input 
    encryptedString = ""
    for i in message:
        encryptedString += str(ord(i))
        encryptedString += " "
    return(encryptedString)
print(encrypt(input))#print the encrypted input 
