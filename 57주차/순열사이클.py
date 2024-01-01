import sys
input = sys.stdin.readline
tc = int(input())

def dfs(x):
    visited[x]=1
    for v in g[x]:
        if not visited[v]:
            dfs(v)

for _ in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    g = [ [] for _ in range(n+1)] 
    for i,v in enumerate(arr):# 그래프 연결.
        g[i+1].append(v)
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:# dfs로 방문처리하여 개수 세기.
            dfs(i)
            cnt += 1
    print(cnt)

# 더 빠른 풀이
# 사이클 개수만 구하면 되므로, 입력 받은 배열 만으로, 1->3 연결, 3->7 연결, 7-> 5연결 등과 같은 식으로
# 개수를 세어도 괜찮다.
for _ in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = [0]+arr
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        if visited[i]:
            continue
        cnt += 1
        visited[i]=1
        next = arr[i]
        while not visited[next]:
            visited[next] = 1
            next = arr[next]
    print(cnt)