n = int(input())
arr = list(input().split())

dict = {'U':0,'D':1,'L':2,'R':3}
sx,sy = 1,1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in arr:
    nx = sx + dx[dict[i]]
    ny = sy + dy[dict[i]]
    if 1 <= nx <= n and 1 <= ny <= n:
        sx,sy = nx,ny

print(sx,sy)
# 이코테 구현 예제