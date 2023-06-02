#Create a program that generates multiple text files by iterating over the filenames list. 
#The text Hello should be written inside each generated text file.

file_names =  ['../doc.txt','../presentation.txt','../report.txt']
for file_name in file_names:
    file = open(file_name,'w')
    file.write("hello")
    file.close()
    
