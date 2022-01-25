a = int(input("input a:"))
b = int(input("input b:"))
# c=b%10
# d=(b%100)//10
# e=b//100
# print(a*c)
# print(a*d)
# print(a*e)
# print(a*b)

print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)

