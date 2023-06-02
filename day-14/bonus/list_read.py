#list1=[1,2,3,4,5,6,-6,-5,-4,-3]

list2=[10,20,30,40,-40,-30,-20,-10]
total_items=len(list2)
i=0
item2=0
while i <= total_items-1:
    for item in list2:
        item=list2[i]
        item2=item2+item
        i=i+1
print(item2)
