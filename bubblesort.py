list1 = [2,6,12,4,8,0,9]
print(list1)
for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if(list1[j]>list1[j+1]):
            temp= list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print(list1)
        
