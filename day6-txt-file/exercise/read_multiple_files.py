#Please download the three text files a.txt, b.txt, and c.txt from the resources. 
# Then, create a program that reads each text file and prints out the content of each in the command line. The expected output would be like the following:

filenames = ['a.txt','b.txt','c.txt']
for files in filenames:
    file=open(files,'r')
    print(file.read())
    file.close()