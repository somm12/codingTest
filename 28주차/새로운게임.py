dx = [0,0,-1,1] # 우 좌 상 하
dy = [1,-1,0,0]
n, k = map(int,input().split())
horse = [] # idx가 곧 k번 말을 뜻하며, [x,y,d] 형태로 저장.
chess = [[[] for _ in range(n)] for _ in range(n)] # x,y 좌표 위에 있는 말 번호들을 담을 체스판.
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

for i in range(k):
    x,y,d = map(int,input().split())
    horse.append([x-1,y-1,d-1]) 
    chess[x-1][y-1].append(i)

cnt = 1

def solve(h_num): # k번 말 이동시키는 함수.
    x,y,d = horse[h_num]
    nx = x+dx[d] # d방향으로 이동.
    ny = y + dy[d]
    if nx <0 or nx >= n or ny < 0 or ny >= n or g[nx][ny] == 2: # 파란색/범위 벗어남.
        if d % 2 == 0: # 좌: 0 or 하: 2일때 (우: 1, 상:3 각각 반대방향)
            d += 1
        else:
            d -=1
        horse[h_num][2] = d  # 방향 바뀐 것 horse에 반영.

        nx = x +dx[d] # 반대방향으로 이동
        ny = y + dy[d]
        # 이동하지 않고 그대로 이기 때문에 True 반환.
        if nx < 0 or nx >= n or ny < 0 or ny >= n or g[nx][ny] == 2: # 그래도 범위 벗어남 or 파란색.
            return True
    tmp = [] # 원래 있던 위치에서 해당 말과 말위에 있는 모든 말을 담을 배열.
    for i,v in enumerate(chess[x][y]):
        if v == h_num: # 체스판 위에 있는 말 중, 현재 말을 찾으면,
            tmp  = chess[x][y][i:] # 그 위로 모든 말을 배열에 담는다.
            chess[x][y] = chess[x][y][:i] # 이동 하고 나면 원래 부분은 그 전까지 할당.
            break
    if g[nx][ny] == 1: # 이동할 칸이 빨간색이면, 거꾸로.
        tmp.reverse()
    
    for i in tmp: # 이동하고 난 후 결과 반영.
        horse[i][0], horse[i][1] = nx,ny # 말의 위치가 변경.
        chess[nx][ny].append(i) # 이동할 칸 부분 체스판 위에 추가됨.
    if len(chess[nx][ny]) >= 4: # 이동한 좌표의 말 개수가 4개이상이면 False 반환.
        return False
    return True
while True:
    if cnt > 1000:# 1000번 넘으면 -1
        print(-1)
        break
    flag = False
    for i in range(k):
        if not solve(i): # 이동시 칸에 4개이상 말이 생기면 종료.
            flag = True
            break
    if flag:
        print(cnt) # 종료될때의 턴의 번호 출력.
        break
    cnt += 1