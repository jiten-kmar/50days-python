#Create a program that reads that file and prints out its text. 
#The first letter of each word in the output should be uppercase.
file_read = open('essay.txt','r')
cap = file_read.read()
print(cap.title())
file_read.close()

# Write a program that reads the essay.txt file and returns the number of 
# characters contained in the file.
file_read=open('essay.txt','r')
num_of_char = len(file_read.read())
print(num_of_char)
file_read.close()
