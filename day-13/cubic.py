#Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.
lit_in = int(input("Enter the liters : "))

def cubicval(lit_in):
    cubic_val = float(lit_in/1000)
    return cubic_val

cval = cubicval(lit_in)
print(cval)








