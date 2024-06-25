from math import *
def isprime(n):
    if n <= 1: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True
arr, prim = list(range(1, int(input())+1)), 0
for i in arr:
    if isprime(i): prim += 1
if prim % 2 == 0: print("Bobur")
else: print("Ali")


# num = int(input()) #bu yerda son kiritiladi

# l=[] #tub sonlar saqlanadi

# for a in range (2,num+1): #tub sonlarni saqlaydi
#    b=0

#    c=[x for x in range(1, a+1) if a%x==0]

#    if len(c) == 2:
#       l.append(a)

# if len(l)%2==0: #va qolgan logika
#    print("Bobur")
# else:
#    print("Ali")