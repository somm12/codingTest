from collections import deque

def bfs(places,x,y):
    distance = [[0]*5 for _ in range(5)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque()
    q.append((x,y))
    visited = [[0]*5 for _ in range(5)]
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny < 5 and not visited[nx][ny] and places[nx][ny] != 'X':# 파티션 만나면 더이상 볼 필요없기에 조건문에 넣어줌.
                
                distance[nx][ny] = distance[x][y] + 1
                if distance[nx][ny] < 3:
                    q.append((nx,ny))
                    if places[nx][ny] == 'P':
                        return False
                visited[nx][ny] = 1
    return True
            
        
def solution(places):
    answer = []
    for place in places:
        g = []
        for arr in place:
            g.append(list(arr))
        p = []
        for i in range(5):
            for j in range(5):
                if g[i][j] == 'P':
                    p.append((i,j))
        for x,y in p:# 미리 배열에 좌표값 할당하는 방법으로 하나라도 False면 break 가능하게함.
            if not bfs(g,x,y):
                answer.append(0)
                break
        else:
            answer.append(1)
    
    return answer
# 거리두기 확인하기