filenames = ["1.Raw Data.txt", "2.Raw Data.txt", "3.Raw Data.txt"]
for filename in filenames:
    filename= filename.replace('.', '-', 1)
    print(filename)
