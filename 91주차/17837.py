dx = [0,0,-1,1]# 우 좌 상 하.
dy = [1,-1,0,0]
n,k = map(int,input().split())

g = []
horse = [[[] for _ in range(n)] for _ in range(n)]
di = {}
for _ in range(n):
    g.append(list(map(int,input().split())))
    
for num in range(1,k+1):
    x,y,d = map(int,input().split())
    horse[x-1][y-1].append(num)# 3차원 배열에 각 체스판에 말의 상태를 나타냄. 번호만!
    di[num]= d-1# 방향 지정.

def blueOrOut():# 파란색이나 격자밖을 벗어난 경우.
    di[num] ^= 1# 방향 전환
    d = di[num]
    nx,ny = x+dx[d],y+dy[d]
    if inRange(nx,ny):
        if g[nx][ny] == 0:# 흰색인 경우.
            tmp = horse[x][y][m:]
            horse[x][y] = horse[x][y][:m]
            for v in tmp:
                horse[nx][ny].append(v)
        elif g[nx][ny] == 1:# 빨간색인 경우.
            tmp = horse[x][y][m:]
            horse[x][y] = horse[x][y][:m]
            while tmp:
                horse[nx][ny].append(tmp.pop())# 반대 순서로 append
    # 또 파란색 이나 격자밖이라면 그대로.
    
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def find(num):# num번 말 위치 찾고, 해당 위치에서 몇번째에 있는가. 말이 이동할 때, 그 위에 쌓인 말도 같이 이동함.
    for i in range(n):
        for j in range(n):
            for m in range(len(horse[i][j])):
                if horse[i][j][m] == num:
                    return [i,j,m]
turn = 1
isDone = False
while True:
    if turn > 1000:
        print(-1)
        break
    for num in range(1,k+1):
        x,y,m = find(num)
        d = di[num]
        nx,ny = x+dx[d],y+dy[d]
        if inRange(nx,ny):
            if g[nx][ny] == 0:# 흰색
                tmp = horse[x][y][m:]
                horse[x][y] = horse[x][y][:m]
                for v in tmp:
                    horse[nx][ny].append(v)
            elif g[nx][ny] == 1:# 빨간
                tmp = horse[x][y][m:]
                horse[x][y] = horse[x][y][:m]
                while tmp:
                    horse[nx][ny].append(tmp.pop())
            else:# 파란색
                blueOrOut()
        else:# 격자밖
            blueOrOut()
                
                    
    
        nx,ny,_ = find(num)
        if len(horse[nx][ny]) >= 4:# 쌓인 말들이 4개이상이면 종료.
            isDone = True
            break
    if isDone:# 이미 게임 종료.
        print(turn)
        break
   
    turn += 1
# 백준 새로운 게임2