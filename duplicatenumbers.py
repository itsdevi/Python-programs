num = [3,4,1,5,3,6,3,3,7,1]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]==num[j]):
            print(" is duplicate")
            flag=1
            break
    if(flag==1):
        break
    else:
        print("no duplicates")