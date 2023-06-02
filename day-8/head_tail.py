# The user runs the program. The program asks the user to enter "head" or "tail". 
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail".
# The user does the same over and over again.
# In each cycle, the program should return the current percentage of heads in the program, 
# similar to what you see in the screenshot above. 
# Also, you should write each user entry (i.e., head or tail) in a text file using a 
# with-context manager, one entry per line.

import random
total = 0
flip=1
tails=0
heads=0
hit = int(input("how many times you want to try "))
while flip <= hit:
# ans = random.randint(0, 1)	
    print("Flip the coin: ")
    ans = random.randint(0, 1)
    total= total + 1 
    if ans == 0:
        print("Entered value is tail")
        tails = tails + 1
    else:
        print("Entered value is Head")
        heads = heads + 1
    flip = flip + 1
    print("answer is:", ans)
    print("total is", total)
print("%  of heads is:", ((heads*100/total)))


while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()
    
    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)
    
    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")
