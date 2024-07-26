num=65
for i in range(0,6):
    for j in range(i):
        print(chr(num), end=" ")
       # j=j+1
        num=num+1
    print()

# or

# letter = ord('A')
# for i in range(0,6):
#     for j in range(i):
#         print(chr(letter), end=" ")
#         letter+=1
    
#     print()