from collections import deque
n = int(input())
parent = list(map(int,input().split()))

deleteNode = int(input())
leafToRoot = []
des = [0]*n # 자손개수
answer = 0
g = [[] for _ in range(n)]# 연결 정보 

for idx,v in enumerate(parent):# 루트 찾기.
    if v == -1:
        root = idx
        break

for idx, v in enumerate(parent):
    if v == -1:
        continue
    g[idx].append(v)# 연결 상태 할당하기.
    g[v].append(idx)

def bfs(x):# 루트 부터 리프노드 까지 순회하는 배열만들기.
    q = deque()
    q.append(x)
    visited = [0]*n
    visited[x] =1
    while q:
        x = q.popleft()
        leafToRoot.append(x)
        for v in g[x]:
            if not visited[v]:
                visited[v] = 1
                q.append(v)

bfs(root)
leafToRoot.reverse()# 리프부터 루트까지 변경


for v in leafToRoot:# 각 노드의 자손개수 모으기.
    if v == root:
        continue
    
    des[parent[v]] += 1
    des[parent[v]] += des[v]

# 삭제하기-> 삭제된 노드 부모는 그만큼 줄어든다.
des[parent[deleteNode]] -= (des[deleteNode]+1)

visited = [0]*n
def dfs(x):
    des[x] = -2
    visited[x] = 1
    for v in g[x]:
        if not visited[v] and v != parent[x]:
            dfs(v)

dfs(deleteNode)# 삭제 노드 포함 그의 자식노드까지 -2를 할당해서 삭제시키기.

for v in des:
    if v == 0:
        answer += 1
print(answer)



