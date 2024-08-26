R,C,M = map(int,input().split())
g = [[[] for _ in range(C)] for _ in range(R)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    if d <= 2: # 상 하 => 한 싸이클 RorC -1 *2 로 나누면 더 적은 칸으로 speed 만들 수 있음.
        s %= (R -1) * 2; 
    elif d<= 4:# 우 좌
        s %= (C -1) * 2;
    g[r-1][c-1].append([s,d-1,z])

def catch():
    global answer,g
    for x in range(R):
        if len(g[x][y]) > 0:
            _,_,z = g[x][y][0]
            answer += z
            g[x][y] = []
            break

def sMove():
    global g
    tmp = [[[] for _ in range(C)] for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            for s,d,z in g[i][j]:
                row,col = i,j
                speed = s # 초기 값 저장.
                while True:# 끝에 도착할 때 마다 방향 전환.
                    nx,ny = row + dx[d]*s, col +dy[d]*s# 남은 속력만큼, 현재 방향으로 이동.
                    if 0 <= nx < R and 0 <= ny < C:# 드디어 범위 내 이동이 되었다면 끝.
                        break
                    if d <= 1: #상 하
                        if nx < 0:
                            s -= row
                            row = 0
                        else:
                            s -= (R-1-row)
                            row = R-1
                    else:# 좌우
                        if ny < 0:
                            s -= col
                            col = 0
                        else:
                            s -= (C-1-col)
                            col = C-1
                    
                    d ^= 1 #  방향 전환. 1 -> 0, 0 -> 1, 2->3, 3->2
                tmp[nx][ny].append([speed,d,z])
                
                        
    g = tmp

def eat():
    global g
    for i in range(R):
        for j in range(C):
            if len(g[i][j]) > 1:# 가장 큰 물고기가 다 잡아 먹음
                g[i][j].sort(key = lambda x: -x[2])
                s,d,z = g[i][j][0]
                g[i][j] = [[s,d,z]]
                

answer = 0
for y in range(C):
    catch()
    sMove()
    eat()
   
print(answer)
# 백준 낚시왕.
# 반복 패턴 부분은 길이를 나누어 떨어진 부분으로 반복을 줄인다.
# 지그재그 부분은, 끝 지점에서 방향 전환하기.