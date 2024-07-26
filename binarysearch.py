#to find given card with min number of turns

cards = [2,5,7,1,9,12]
cards.sort()

n = int(input("Enter key"))

length= len(cards)
f= 0
l =length-1
while(f<=l):
    mid = (f+l)//2
    if(n==cards[mid]):
        flag=1
        print("found at ",mid)
        break
    elif(n>cards[mid]):
        f=mid+1
    elif(n<cards[mid]):
        l=mid-1
if(flag!=1):
    print("NOT found")