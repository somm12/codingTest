c = 100
s = 100

n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    if a > b:
        s -= a
    elif a < b:
        c -= b
    
print(c)
print(s)