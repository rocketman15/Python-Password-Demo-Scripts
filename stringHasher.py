import hashlib
input = input("enter a string to be hashed ")
def hashString(string):
    result = hashlib.md5(string.encode())
    return(result.hexdigest())
print(hashString(input))