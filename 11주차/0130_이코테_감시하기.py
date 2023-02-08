from itertools import combinations
from copy import deepcopy
n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

g = []
arr = []
for i in range(n):
    g.append(list(input().split()))
    for j in range(n):
        if g[i][j] == 'X':
            arr.append((i,j))
def dfs(x,y,d):
    nx = x + dx[d]
    ny = y + dy[d]
    
    while 0 <= nx < n and 0 <= ny < n and t[nx][ny] != 'O':
        if t[nx][ny] == 'S':
            return True
        else:
            nx += dx[d]
            ny += dy[d]
    return False
        
res = 'NO'
def process():
    for i in range(n):
        for j in range(n):
            if t[i][j] == 'T':
                for k in range(4):
                    if dfs(i,j,k):
                        return True
    return False

for obstacle in combinations(arr,3):
    t = deepcopy(g)
    for i,j in obstacle:
        t[i][j] = 'O'
    if not process():
        res = 'YES'
        break
print(res)
