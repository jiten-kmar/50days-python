contents = ["All carrots are to be sliced.","the carrots are reportedly sliced. ", "The slicing is well prepared"]

filenames = ["doc.txt","report.txt","presentation.txt"]

# doc_file = open('doc.txt','w')
# doc_file.writelines(contents[0])
# doc_file.close()

# doc_file = open('report.txt','w')
# doc_file.writelines(contents[1])
# doc_file.close()

# doc_file = open('presentation.txt','w')
# doc_file.writelines(contents[2])
# doc_file.close()

for content,filename in zip(contents,filenames):  #zip is used to merge them together
    file=open(f" {filename}",'w')
    file.write(content)
    file.close()
    