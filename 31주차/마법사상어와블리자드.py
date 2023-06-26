dx = [-1,1,0,0] # 구슬 파괴 상하좌우(1,2,3,4) 방향.
dy = [0,0,-1,1]
mx = [0,1,0,-1]#좌 우 하 상 => 상어 위치 부터 0,0까지 구슬를 보는 방향.
my = [-1,0,1,0]

n,m = map(int,input().split())
sx,sy = n//2,n//2 # 상어위치.


marble = [0] # 칸 번호는 1번 부터 시작이므로, 0 초기화.
num = {} # 좌표에 따른 칸번호 표현
location= {} # 칸번호에 따른 좌표 표현.

board = []
answer = [0,0,0,0] # 각 1번 2번 3번 파괴된 구슬 개수 세기.
for _ in range(n):
    board.append(list(map(int,input().split())))

def init(): # 로직 구현에 필요한 부분 초기화
    global marble, num,location
    tmp = 0
    idx = 0
    nx, ny = sx,sy
    number = 1 # 칸번호 1번부터
    # 1 1 2 2 | 3 3 4 4 |5 5 ... 좌 하 우 상 순서로. 각 x칸씩 방향 이동.
    while 0 <= nx < n and 0 <= ny < n: # 0,0까지 진행.
        idx = idx%4
        if idx % 2 == 0:
            tmp += 1
        for _ in range(tmp):
            nx += mx[idx]
            ny += my[idx]
            if 0 <= nx < n and 0 <= ny < n: # 초기화.
                num[(nx,ny)] = number
                location[number] = (nx,ny)
                marble.append(board[nx][ny]) # 칸번호(인덱스)에 따른 구슬 번호 할당.
                number += 1

        idx += 1

def destroy():# 거리가 s이하인 d방향으로 구슬 파괴
    global marble,d,s
    nx,ny = sx,sy
    for _ in range(s):
        nx += dx[d]
        ny += dy[d]
        room = num[(nx,ny)]
        
        marble[room] = -1
def move():# 파괴가 되면서 -1 부분 없애고 구슬 정리하기.
    global marble
    
    delCnt = marble.count(-1)
    marble = [value for value in marble if value != -1]
    
    marble.extend([0]*delCnt) # 사라진 부분 개수만큼 또 0으로 채운다.
    
    

def explosion():# 구슬 폭발. 연속 4개이상이라면 -1 할당
    global marble,answer
    
    now = 0
    cnt = 0
    start = 0
    flag = False
    
    for i in range(n**2):
        if now != marble[i]:
            if cnt >=4:
                flag = True
                answer[now] += cnt
                for j in range(start,i):
                    marble[j] = -1
            cnt = 1
            now = marble[i]
            start = i
        else:           
            cnt += 1
    return flag

def change():# 구슬 개수를 그룹으로 나누어. 각 그룹 내 번호 개수와 번호 두 개를 가지고 다시 marble update
    global marble # 단, n*n 칸 넘어가면 자른다. 중요.
    
    new = [0]
    
    group = []
    for i in range(1,n**2):
        if not group:
            group.append(marble[i])
        elif group[0] == marble[i]:
            group.append(marble[i])
        else:
            new.append(len(group))
            new.append(group[0])
            group = [marble[i]]
        
    marble = [0]*(n*n)
    for i in range(len(new)):
        if i >= n*n: # 칸 수를 넘어간다면 자른다.
            break
        marble[i] = new[i]
    
# 좌 하 우 상 방향으로, 규칙으로 로직을 수행하는데 필요한 부분 초기화. 
init()

for _ in range(m):
    d,s =map(int,input().split())
    d -= 1
    destroy()
    move()    
    while True:# 구슬 폭발할게 없을 때까지 반복.
        if explosion():
            move()
        else:
            break
    change()
    
print(answer[1]+answer[2]*2+ answer[3]*3)