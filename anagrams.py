def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
answer= are_anagrams(str1,str2)
if(answer):
    print("They are anagrams")
else:
    print("They are not anagrams")
