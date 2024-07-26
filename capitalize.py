# input a string and return with each word's first letter capitalized

str1= input("enter string")
str2=""
list1 = str1.split()
for a in list1:
    str2 += a.capitalize()+ " "
print(str2)