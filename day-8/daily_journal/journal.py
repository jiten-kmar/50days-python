import datetime
dt = input("Enter the date: ")
mood = int(input("Enter your mood today from 1 to 10: "))
thoughts = input("let your thoughts flow here: \n",)

with open(f"{dt}.txt",'w') as file:
    file.write(thoughts)
    