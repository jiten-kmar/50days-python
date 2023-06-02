def read_file():
    with open('file.txt','r') as file_local:
        read_fl = file_local.readlines()

    values=read_fl[1:]
    values = [float(i) for i in values]
    avg = sum(values)/len(values)
    return avg


file_read=read_file()
print(file_read)