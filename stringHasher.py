import hashlib# import the hashlib library 
input = input("enter a string to be hashed ") # get user input
def hashString(string):
    result = hashlib.md5(string.encode())
    return(result.hexdigest())
print(hashString(input))#hash the string
