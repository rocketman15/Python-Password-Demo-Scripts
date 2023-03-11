user_password = "Like"
user_input = input("enter the correct password to access the program ")
def compare_passwords(correct_password, user_input):
    if user_input == correct_password:
        return(1)
    else:
        return(0)
def main():
    print("unlock successful")
if compare_passwords(user_password, user_input) == 1:
    main()
else:
    print("sorry. incorect password. Like the video, then try again")