waiting_list = ['sen','ben','john']
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index+1}. {item.capitalize()}"
    print(row)

for i, j in enumerate("abcd"):
    phrase = f"Printing {i * 5}"
    print(phrase)

ips = ['100.122.133.105', '100.122.133.111']
idx = int(input("Enter the index of the IP you want: "))
print(ips[idx])

menu = ["pasta", "pizza", "salad"]
user_choice = int(input("Enter the index of the item: "))
message = f"You chose {menu[user_choice]}."
    print(message)

menu = ["pasta", "pizza", "salad"]
for i, j in enumerate(menu):
    print(f"{i}.{j}")