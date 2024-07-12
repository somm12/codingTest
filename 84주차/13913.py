from collections import deque
n,k =map(int,input().split())
MAX = 100000
prev = [0]*(MAX+1)
def bfs(x):
    visited = [0]*(MAX+1)# 최대 범위는 10만이기 때문에,
    q = deque()
    q.append(x)
    visited[x] = 1 # 방문처리 체크 겸 + 최단 거리 시간 저장.
   
    if n == k:# 값이 같을 때, 예외처리.
        print(0)
        print(n)
        return

    while q:
        now = q.popleft()
        for nxt in [now-1,now+1,2*now]:
            if 0<= nxt <= MAX:
                if not visited[nxt]:# 방문이 처음일 때.
                    q.append(nxt)
                    visited[nxt] = visited[now] + 1# 걸리는시간 + 1
                    prev[nxt] = now # 이전 방문 번호 저장.
                
    print(visited[k]-1)
    arr = [k]
    tmp = k
    while True:
        nxt = prev[tmp]
        arr.append(nxt)
        if nxt == n:
            break
        tmp = nxt

    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end =' ')

bfs(n)

# 백준 숨바꼭질 4.