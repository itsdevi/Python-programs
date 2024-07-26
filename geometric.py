n = int(input("Enter limit"))
r = float(input("Enter ratio"))
a= int(input("Enter first term"))
print("\n Series\n")
sum=0
for i in range(1,n):
    term = a*(r**i)
    sum=sum+term
print("sum = ",sum)
