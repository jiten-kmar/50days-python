#Write a program that gets a list of names from the user and returns the number of names given.
# You are encouraged to use a function. Here is how the program would work:

names=input("Enter the names seperated by commas, no spaces:")
number=[]
def leng(names):
    number = len(names.split(","))
    return number

num=leng(names)

print(num)