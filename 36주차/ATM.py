n = int(input())
arr = list(map(int,input().split()))
arr.sort()# 최소시간으로 기다리려면, 정렬.
tmp = 0 # 인출 시간 축적.
ans = 0
for i in arr:
    ans += (tmp+i)
    tmp+= i
print(ans)
# 지금까지 인출하는데 걸린시간 + 내가 인출하는데 걸린 시간 => 축적되는 형태.
# 백준 그리디 문제