import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
n = int(input())
g = [[] for _ in range(n+1)]

visited = [0]*(n+1)

for _ in range(n):
    a,b,c = map(int,input().split())
    g[a].append(b)
    g[a].append(c)
   
cnt1 = 0
cnt2 = 0

def dfs1(x):
    global cnt1
    l,r = g[x]
    if l != -1 and not visited[l]:
        visited[l]= 1
        cnt1 += 1
        dfs1(l)
    if r != -1 and not visited[r]:
        visited[r] = 1
        cnt1 += 1
        dfs1(r)

def dfs2(x):# 오른쪽으로 가는 간선의 개수.
    global cnt2
    _,r = g[x]
    if r != -1 and not visited[r]:
        visited[r] =1
        dfs2(r)
        cnt2 +=1

dfs1(1)
visited = [0]*(n+1)
dfs2(1)
print(cnt1*2-cnt2)
# 오른쪽으로 가는 간선만 한번만 방문함!!
# 전체 방문 왕복 - 오른쪽으로 가는 간선 개수.


