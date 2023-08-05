n = int(input())
arr = []
for _ in range(n):
    v = int(input())
    arr.append(v)
arr.sort(reverse=True)
for v in arr:
    print(v,end=' ')
# 이코테 정렬 예제 1번