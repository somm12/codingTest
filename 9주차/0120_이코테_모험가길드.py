n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0 # 총 그룹수
cnt = 0 # 현재 그룹 명수
print(arr)
for i in arr:
    cnt += 1
    if cnt >= i:
        cnt = 0
        result += 1

print(result)