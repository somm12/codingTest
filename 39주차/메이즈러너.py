n,m,k = map(int,input().split())
g = []
people = []
for _ in range(n):
    g.append(list(map(int,input().split())))

for _ in range(m):
    a,b = map(int,input().split())
    people.append((a-1,b-1))

ex,ey = map(int,input().split())
ex -=1# (1,1)부터 시작이므로, -1 하기.
ey -= 1

dx = [-1,1,0,0] # 상하좌우.
dy = [0,0,-1,1]
answer = 0# 이동한 총 거리

def move():# 모든 참여자들 이동.
    global people, answer
    new = []#  참여자들이 이동한 위치를 담을 새로운 배열.
    for x,y in people:
        dist = abs(ex-x) + abs(ey-y)# 현재 위치와 탈출구 최단 거리.
        cand = []# 이동 가능한 모든 후보를 담는 배열.
        for i in range(4):# 상하좌우 
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 0:# 벽이 아니고 범위내라면
                tmp = abs(nx-ex)+abs(ny-ey)# 해당 위치가 탈출구와 더 가까워지는 칸인지 확인
                if dist > tmp:
                    cand.append((nx,ny,i))# 후보에 추가.
        if cand:# 혹시 이동이 가능하면
            cand.sort(key=lambda x:x[2])# 상,하를 우선순위로 두어 정렬.
            nx,ny,d= cand[0]
            if [nx,ny] != [ex,ey]:# 이동할 칸이 탈출구가 아니라면! 이동할 칸의 좌표 추가.
                new.append((nx,ny))
            answer += 1# 거리 +1.
        else:
            new.append((x,y)) # 만약. 이동을 할 수 없으면 그대로.
    people = new# 참여자들 정보 update

def findSquare():# 탈출구와 최소 한명의 참여자를 포함하는 정사각형 만들기.
    
    for L in range(2,n+1):# 정사각형 길이는 최소 2
        for x in range(n):# 정사각형 좌상단 시작점 행
            for y in range(n):# 시작점 열
                if x+L <= n and y+L <= n:# index out of range 에러를 피하기 위함. 시작점+길이 => 최대 n.
                    for i,j in people:# 한 명의 참여자라도 범위 내에 포함된다면,
                        if x <= i < x+L and y <= j < y + L:
                            if x <= ex < x+L and y <= ey < y+L:# 탈출구도 포함 된다면,
                                return [x,y,L] # 시작점 x,y와 정사각형 길 L를 반환.
    # 길이가 작고 > 좌상단 행이 작고 > 좌상단 열이 작은 순으로 사각형 찾기.
    

def rotate(x,y,L):# x,y 시작점 L 길이 정사각형 회전.
    global ex,ey, g, people
    newPeople = []# 회전하면서 참여자들의 바뀐 좌표를 담을 배열
    new = [[0]*n for _ in range(n)]# 바뀐 격자판 정보를 담을 배열
    for i in range(n):
        for j in range(n):
            new[i][j] = g[i][j]
    flag= True# 탈출구 업데이트. ** 탈출구 한 번 업데이트가 되고 다시 업데이트가 될 수 있으므로, 신호 만들기.
    
    for i in range(L):# L 길이 정사각형.
        for j in range(L):
            px,py = i+x,j+y # 시작점 x,y 반영.
            nx,ny = j+x, L-1-i+y# 바뀐 위치 반영(각 x,y 더하기**). j, n-1-i = i,j 공식.
            if g[px][py] > 0:# 벽 내구성 -1
                g[px][py] -= 1
            
            new[nx][ny] = g[px][py] # 회전하기

            if [ex,ey] == [px,py] and flag:# 출구 좌표 회전.(회전 후 바뀐 값이 다시 또 바뀔 수 있음에 유의.)# 괄호 제대로 쓰기.
                flag = False
                ex,ey = nx,ny
            
         
            for a,b in people:# 같은 좌표 가능. 
                if (a,b) == (px,py):# 참여자들 좌표 회전하면서 이동됨. # !!!!! 괄호 조심.
                    # 혹시 정사각형 내부에 해당 된다면, 회전된 좌표로 append.
                    newPeople.append((nx,ny))
    
    for a,b in people:# 나머지 작은 정사각형에 포함 안되는 참여자들 좌표도 새로운 배열에 옮기기.
        if not (x <= a < x+L and y <= b < y+L):
            newPeople.append((a,b))
    
    people = newPeople# 새로운 배열 update
    g = new# 격자판 update


    

for nth in range(1,k+1):
    move()# 모두 이동
    if len(people) == 0:# 이동 후, 이미 탈출 모두 했다면 종료.
        break
    x,y,L = findSquare()# 가장 정사각형 부분 찾기(탈출구, 최소 참여자 한명 포함)
    rotate(x,y,L)# 회전.
   
    

print(answer)
print(ex+1,ey+1)
# 코드트리 삼전 기출.