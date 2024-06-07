from collections import deque
k,m =map(int,input().split())
g = []
for _ in range(5):
    g.append(list(map(int,input().split())))
info = list(map(int,input().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
idx = 0

def inRange(x,y):
    return 0 <= x < 5 and 0 <= y < 5

def search():
    cand = []
    for x in range(3):# 시작점이 될 수 있는 지점 모두.
        for y in range(3):
            for a in [90,180,270]:# 3가지 회전 방향 중  하나.
                v = firstValue(x,y,a)# 최초 가치 구하기.
                cand.append((v,a,y+1,x+1))# 가치 많고, 각도가 작고, 중심 열이 작고, 중심 행이 작은 순.
    cand.sort(key =lambda x:(-x[0],x[1],x[2],x[3]))
    value,a,y,x = cand[0]
    if value == 0:# 최초 가치가 없다면, 턴 종료.
        return False
    return [x-1,y-1,a]# 중심좌표였으므로, -1해서 시작점 좌표로 만들기.

def rotate(sx,sy,tmp):
    t = [v[:] for v in tmp]
    n = 3
    for x in range(n):
        for y in range(n):
            t[sx+ y][sy+ n - 1 -x] = tmp[sx+ x][sy+ y]
    return t

def firstValue(sx,sy,a):
    tmp = [ar[:] for ar in g]

    for _ in range(a//90):
        tmp = rotate(sx,sy,tmp)

    return cntGroup(tmp)

def cntGroup(b):# 최초 가치를 찾을 때, 3개이상으로 이뤄진 덩어리가 있는지 체크.
    visited =[[0]*5 for _ in range(5)]
    total =0
    for x in range(5):
        for y in range(5):
            if not visited[x][y]:
                q = deque()
                q.append((x,y))
                visited[x][y] = 1
                num = b[x][y]
                cnt = 0
                while q:
                    x1,y1 = q.popleft()
                    cnt += 1
                    for i in range(4):
                        nx,ny = x1+dx[i],y1+dy[i]
                        if inRange(nx,ny) and not visited[nx][ny] and b[nx][ny] == num:

                            q.append((nx,ny))
                            visited[nx][ny] = 1
                if cnt >= 3:
                    total += cnt
    return total
def bfs(x,y,visited,tmp):# 3개이상의 덩어리를 찾고. 그 좌표 정보를 반환.
    arr = []
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    num = tmp[x][y]
    while q:
        x,y =q.popleft()
        arr.append((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and tmp[nx][ny] == num:
                q.append((nx,ny))
                visited[nx][ny] = 1
    return arr

def makingValue(ret):
    global answer,idx,g
    sx,sy,angle = ret
    tmp = [ar[:] for ar in g]
    for _ in range(angle//90):# 90 도를 나누어 몫만큼 회전을 여러번 한다. 270은 3번.
        tmp = rotate(sx,sy,tmp)


    while True:
        visited =[[0]*5 for _ in range(5)]
        flag = False
        for x in range(5):
            for y in range(5):
                if not visited[x][y] and tmp[x][y] > 0:
                    arr = bfs(x,y,visited,tmp)
                    if len(arr) >= 3:
                        flag = True
                        answer += len(arr)
                        for i,j in arr:
                            tmp[i][j] =0
        if not flag:# 유적이 만들어지지 않는다면 그만 찾기.
            break

        for y in range(5):# 열이 작고, 큰 행 순서대로 채우기.
            for x in range(4,-1,-1):
                if tmp[x][y] == 0:
                    tmp[x][y] = info[idx]
                    idx += 1

    g= tmp


for _ in range(k):
    answer =0
    ret = search()# 1회차 취득 가치가 제일 크고,, 우선순위대로 회전 시작점과, 회전 각도를 찾음.
    if ret == False:# 가치가 1개도 없다면 종료.
        break

    makingValue(ret)# 회전할 부분을 두고, 유적을 취득(사라지고 채우고 반복. 사라질 부분 없을 때까지)

    print(answer,end=" ")
# 코드트리 문제.
# 같은 변수 사용 주의