n,k = map(int,input().split())
horse = []
color = []
chess = [[[] for _ in range(n)] for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(n):
    color.append(list(map(int,input().split())))

for i in range(k):
    a,b,c = map(int,input().split())
    horse.append([a-1,b-1,c-1])
    chess[a-1][b-1].append(i)

turn = 1

def move(num,x,y,d):
    nx = dx[d] + x
    ny = dy[d] + y
    
    for i,v in enumerate(chess[x][y]):
        if num == v:
            tmp = chess[x][y][i:]
            chess[x][y] = chess[x][y][:i]
            break
    if color[nx][ny] == 1:
        tmp.reverse()
    for v in tmp:# 옮기려는 말들 모두 위치 변한거 반영.
        horse[v][0],horse[v][1] = nx,ny
        chess[nx][ny].append(v)
    
    if len(chess[nx][ny]) >= 4:# 말이 4개이상 되는 순간! 종료.
        return False
    return True


while True:
    if turn > 1000:
        print(-1)
        break
    flag= False
    for i, v in enumerate(horse):
        x,y,d = v
        nx = x+dx[d]
        ny = y +dy[d]
        if not(0<=nx < n and 0<=ny < n) or color[nx][ny] == 2:
            if d%2 == 0:
                d +=1
            else:
                d-=1
            horse[i][2] = d
            nx = x+dx[d]
            ny = y +dy[d]
            if not(0<=nx < n and 0<=ny < n) or color[nx][ny] == 2:
                continue
            else:
                if not move(i,x,y,d):
                    flag = True
                    break
        else:
            if not move(i,x,y,d):
                flag= True
                break
    if flag:
        print(turn)
        break
    turn += 1

