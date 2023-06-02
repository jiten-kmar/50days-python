password = input ("Enter the password: ")
count=0
if len(password)>=8:
    if password.isalnum():
        for character in password:
            if character.isdigit():
                count=count + 1
        for character in password:
            if character.isupper():
                count+=1
    print("it is strong password")
else:
    print("it is not strong password")
    