a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sum(a)
b = sum(b)
if a >= b:
    print(a)
else:
    print(b)
