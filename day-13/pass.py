#Create a script that asks the user to enter a password.
# Then create a function that checks the strength of the user password.
# The function should return Strong Password if all of the following conditions are true:
#Eight or more characters
#At least one uppercase letter.
#At least one digit.

passd = (input("Enter the password : "))
def strong_pass(passd):
    if len(passd)>=8 and passd.isalnum() and any(ch.isupper() for ch in passd):
        print("strong password")
    else:
        print("It's not a strong password")

    return passd

paval = strong_pass(passd)
