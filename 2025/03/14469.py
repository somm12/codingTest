n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort()
time = 0
for a,b in arr:
    total = max(time, a) + b
    time = total
print(time)
# 백준 소가 길을 건너간 이유 3 

