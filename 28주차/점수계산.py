
n = int(input())
arr = list(map(int,input().split()))
total = 0 
tmp = 0
for i in arr:
    if i == 1:
        tmp += 1
        total += tmp
    else:
        tmp = 0
print(total)
# 백준 - 점수계산 문제