num = int(input("Enter number"))
rev=0
n=num
while n>0:
    dig= n%10
    rev = rev*10+dig
    n=n//10
if num==rev:
    print("Palindrome")
else:
    print("Not Palindrome") 