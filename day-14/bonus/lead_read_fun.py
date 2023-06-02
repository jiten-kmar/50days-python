list2=[10,20,30,40,-40,-30,-20,-10,20]
total_items=len(list2)
i=0
item2=0
while i <= total_items-1:
    for item in list2:
        item=list2[i]
        item2=item2+item
        i=i+1
print(item2)