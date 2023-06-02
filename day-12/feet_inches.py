feet_inches = input("Please enter feet and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * .3048 + inches * .0254
    return  meters


result = convert(feet_inches)
print((result))