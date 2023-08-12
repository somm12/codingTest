n,m = map(int,input().split())

board = []
dx = [0,1,0,-1]# 구슬 칸번호 순서대로 할당하기 위한 방향 배열. 좌 하 우 상
dy = [-1,0,1,0]

desX = [-1,1,0,0]# d,s 입력 받고 이동하기 위한 방향 배열. 상 하 좌 우
desY= [0,0,-1,1]
answer = [0,0,0,0]# 각 구슬 번호가 파괴된 수를 저장할 배열.
marble = [0] # 인덱스가 곧 칸번호. 구슬 정보를 1차원 배열로 나타냄.
location = {} # {(x,y):칸번호,..}
sx,sy = (n+1)//2-1, (n+1)//2-1# 상어의 위치

lastNum = (n*n)-1# 마지막 칸번호.
for _ in range(n):
    board.append(list(map(int,input().split())))

def init():# 구슬 배열과, location 사전 자료구조 초기화하기.
    global marble, location
    num= 1
    x,y = sx,sy
    cnt = 0
    di = 0
    while True:# 좌 하 우 상 좌 하 우 상 (1칸 1칸 2칸 2칸 3칸 3칸) => 반복. 방향 인덱스가 짝수일 때 cnt +1
        if not (0 <= x < n and 0 <= y < n):
            break
        if di % 2 == 0:
            cnt += 1
        di %= 4
        
        for _ in range(cnt):
            
            x += dx[di]
            y += dy[di]
        
            if (0 <= x < n and 0 <= y < n):
                location[(x,y)] = num
                marble.append(board[x][y])
                num += 1
        di += 1


def destroy():# d방향 s이하 구슬 파괴.
    global marble,d,s
    nx,ny = sx,sy
    for _ in range(s):
        nx += desX[d]
        ny += desY[d]
        if 0 <= nx < n and 0 <= ny < n:
            idx = location[(nx,ny)]
            marble[idx] = 0
def move():# 다시 앞쪽에 빈 부분 뒤 구슬로 채우기.
    global marble
    marble = [v for v in marble if v != 0]# 0이어서 빈 부분 제외

    marble.extend([0]* (lastNum - len(marble)))# 당긴 만큼 사라진 빈 공간 0으로 채움.
    marble = [0]+ marble# 인덱스를 칸번호를 맞추기 위해 0을 추가

def explosion():# 폭발. 폭발 유부 true, false 리턴.
    global marble
    cnt = 0
    start = 0# 어디 부터 같은 구슬 인지 저장하기 위한 변수.
    now = marble[0]# 비교할 구슬 번호
    flag = False
    for i,v in enumerate(marble):
        if now == v:
            cnt += 1
        else:
            if cnt >= 4:# 4개 이상 연속이면 파괴시키기.
                for idx in range(start,i):
                    answer[now] += 1# 폭발된 구슬 개수 세기
                    marble[idx] = 0
                    flag = True
            cnt = 1
            now = v
            start = i
    return flag
def change():# 변화. 그룹을 2개 구슬로 나눔.(개수, 구슬번호.)
    global marble
    new = [0]
    cnt = 0
    now = marble[1]
    for i in range(1, len(marble)):
        if marble[i] == now:
            cnt += 1
        else:
            new.append(cnt)
            new.append(now)
            now = marble[i]
            cnt = 1
    if len(new) > len(marble):# 격자 밖으로 값이 넘친다면 자르기.
        new = new[:len(marble)]
    else:# 부족하게 되면 그만큼 0으로 채운다.
        new.extend([0]* (len(marble)-len(new)))
    
    marble = new


init()

for _ in range(m):
    d,s = map(int,input().split())
    d -= 1
    destroy()
    move()
    while explosion():# 4개 이상 연속 구슬이 나올때까지는 폭발, 앞으로 당기기 반복.
        move()
    change()

print(answer[1]+(2*answer[2])+ (3*answer[3]))
