import sys
sys.setrecursionlimit(100);
input = sys.stdin.readline
r,c = map(int,input().split())
g = []
for _ in range(r):
    g.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer =1

# 아래 코드는 pypy로 제출해야 통과: 반복되는 경로는 탐색해서 오래걸림 ex) 다른 경로지만 백트래킹하고 돌아오면서 ABCD를 반복한다면 시간 낭비.
# def dfs(x,y,L): 
#     global answer
#     answer = max(answer,L)

#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if 0 <= nx < r and 0 <= ny < c:
#             v = ord(g[nx][ny]) -65
#             if not visited[v]:
#                 visited[v] = 1
#                 dfs(nx,ny,L+1)
#                 visited[v] = 0
# dfs(0,0,1)
# print(answer)

stack = set()
stack.add((0,0,1,g[0][0]))# set을 이용하여 시간 줄어듦. 미리 경로를 저장두면서 같은 중복된 경우는 탐색하지 않음.


while stack:
    x,y,cnt,visited = stack.pop()
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < r and 0 <= ny < c and g[nx][ny] not in visited:
            stack.add((nx,ny,cnt+1,visited + g[nx][ny]))
            answer = max(answer,cnt+1)
print(answer)