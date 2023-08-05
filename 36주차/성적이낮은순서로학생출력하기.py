n = int(input())
arr = []
for _ in range(n):
    name, num = input().split()
    num = int(num)
    arr.append((name,num))
arr.sort(key=lambda x:x[1])

for v in arr:
    print(v[0],end=' ')
# 이코테 정렬 예제 2번.