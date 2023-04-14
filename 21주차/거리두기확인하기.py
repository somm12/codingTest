from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(arr,x,y):
    visited = [[0]*5 for _ in range(5)]
    visited[x][y] = 1
    q = deque()
    q.append((x,y,0))
    
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                if arr[nx][ny] != 'X':# 파티션만 아니면 이동가능
                    if arr[nx][ny] == 'P' and dist+1<=2:# 하지만 맨해튼 거리가 2이하고, 사람이 있는지확인.
                        return False
                    visited[nx][ny] = 1
                    q.append((nx,ny,dist+1))
    return True

                    
def solution(places):
    answer = []
    for i in places:
        arr = []
        s = []
        for j in i:
            arr.append(list(j))
        for x in range(5):
            for y in range(5):
                if arr[x][y] == 'P':
                    s.append((x,y))
        for x,y in s:
            if not bfs(arr,x,y):
                answer.append(0)
                break
        else:
            answer.append(1)
        
    return answer