user_password = "Like"# set a string for the password 
user_input = input("enter the correct password to access the program ")# get user input
def compare_passwords(correct_password, user_input):# compare the passwords 
    if user_input == correct_password:
        return(1)
    else:
        return(0)
def main():# put the code that you want to run after a successful unlock here 
    print("unlock successful")
if compare_passwords(user_password, user_input) == 1:
    main()
else:# put the code you want to run after a failed unlock here. 
    print("sorry. incorect password. Like the video, then try again")
