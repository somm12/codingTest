from collections import deque;
import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m, total = map(int,input().split())
done = [[True]*n for _ in range(n)] # 손님 처리 완료 여부를 위한 2차원 배열.
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

cx, cy = map(int,input().split()) # 택시 위치.
cx -= 1 # 행과 열은 번호가 1부터 시작.
cy -= 1
people= {} # 손님의 (출발 위치) : [도착 위치] dictionary.
for _ in range(m):
    a,b,c,d = map(int,input().split())
    people[(a-1,b-1)] = [c-1,d-1]
    done[a-1][b-1] = False

def isFinish(): # 모든 손님이 다 도착했다면 종료시키기.
    for a,b in people:
        if not done[a][b]:
            return False
    return True

def bfs(x,y): # 도착지까지까지 걸리는 최단 거리 반환. 갈 수 없는 경우 또는 연료가 없다면 -1 반환
    global cx,cy,total
    
    q = deque()
    q.append((cx,cy,0))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    while q:
        
        i,j, dis = q.popleft()
        if (i,j) == (x,y):
            return dis # 최단 거리 반환.
        for k in range(4):
            nx = i+ dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0<= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny,dis+1))
    return -1 # 도착지로 이동 할 수 없는 경우( ex: 벽으로 둘러쌓임)


def select(): # 전체 손님과의 최단 거리를 구하고, 해당 손님과의 거리, 출발 및 도착 좌표를 리턴.
    global total
    cand = []
    q = deque()
    q.append((cx,cy,0))
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    
    while q:
        x,y,dis = q.popleft()
        if not done[x][y]:
            ex,ey = people[(x,y)]
            cand.append([dis,x,y,ex,ey])
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny,dis+1))
    cand.sort(key = lambda x : (x[0],x[1],x[2]))
    
    if len(cand) < m or cand[0][0] > total: # 모든 손님을 태울 수 없거나,최단 거리가 연료보다 멀면
        return -1
    
    return cand[0] # 손님 선택 가능하면 해당 정보를 반환. [최단거리, 출발 x, 출발y, 도착x,도착 y]
while True:
    if isFinish():
        print(total)
        break
    cand = select() # 태울 손님 선택.
    
    if cand == -1:# 손님을 태울 수 없는 경우. 접근 불가 일 때/ 모두 연료보다 멀리 있다면
        print(-1)
        break
    dist = cand[0]
    start = [cand[1],cand[2]] 
    end = [cand[3],cand[4]]
    
    total -= dist # 손님있는 곳 까지 이동하면서 연료소모.
    cx,cy = start[0], start[1] # 손님 태우러 이동, 좌표 갱신.
    
    
    dist = bfs(end[0],end[1]) # 도착지 까지 이동.
   
    if dist == -1 or dist > total: # 이동할 수 없거나 연료가 부족하면!! ****
        print(-1)
        break
    total -= dist # 연료소모.
    cx,cy = end[0],end[1] # 도착지로 택시 위치 갱신.
    
 
    total += (dist*2)# 이동한 만큼의 2배 연료충전.
    done[start[0]][start[1]] = True # 손님 도착지까지 이동 후, 처리 갱신.
    m -= 1 # 이동해야할 손님 수 갱신
# 시간 복잡도 : while문 400번 * select문 O(400번*4방향) => 64만.