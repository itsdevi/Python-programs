# num = int(input("Enter number"))
# rev=0
# n=num
# while n>0:
#     dig= n%10
#     rev = rev*10+dig
#     n=n//10
# if num==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome") 

# string palindrome

str1 = input("Enter string: ")
length = len(str1)
p = length - 1
i = 0
is_palindrome = True  
while i < p:
    if str1[i] == str1[p]:
        i += 1
        p -= 1
    else:
        is_palindrome = False 
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
