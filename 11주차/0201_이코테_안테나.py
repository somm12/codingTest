n = int(input())
arr = list(map(int,input().split()))
arr.sort()

a = arr[n//2]
b = arr[n//2 - 1]

s1 = 0
s2 = 0
for i in arr:
    s1 += abs(i-a)
    s2 += abs(i-b)
if s1> s2:
    print(b)
elif s1 < s2:
    print(a)
else:
    print(min(a,b))