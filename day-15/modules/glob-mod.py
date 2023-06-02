import  glob

myfile = glob.glob("files/*.txt")
for filespath in myfile:
    with open(filespath, 'r') as files:
        print(files.read().upper())