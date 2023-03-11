input = input("enter a string to convert to ascii")

def encrypt(message):
    encryptedString = ""
    for i in message:
        encryptedString += str(ord(i))
        encryptedString += " "
    return(encryptedString)
print(encrypt(input))