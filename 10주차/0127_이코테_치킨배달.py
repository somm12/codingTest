from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

city = []
for _ in range(n):
    city.append(list(map(int ,input().split())))
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))
ans = 10**8
for selected in list(combinations(chicken,m)):
    temp = 0
    for x,y in house:
        res = 10**8
        for a,b in selected:
            res = min(res, abs(x-a) + abs(y-b))
        temp += res
    ans = min(ans, temp)
print(ans)