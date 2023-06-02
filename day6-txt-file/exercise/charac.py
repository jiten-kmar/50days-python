#Write a program that reads the essay.txt file and returns the number of characters 
#contained in the file.
readfile = open('essay.txt','r')
lines=readfile.read()
print(len(lines))
