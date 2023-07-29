n,m = map(int,input().split()) # n, 마법 시전할 횟수 m 입력.
sx,sy = n//2,n//2 # 마법사 상어의 위치.

dx = [-1,1,0,0] # 상하좌우 d를 나타낸다.
dy = [0,0,-1,1]

mx = [0,1,0,-1] # 좌 우 상 하 => 칸 번호 순서대로
my = [-1,0,1,0]

answer = [0,0,0,0] # 각 1,2,3번 파괴된 구슬 개수 답을 담을 배열
num = {} # x,y 각 좌표에 해당하는 칸 번호를 초기화하기 위함.
marble =[0] # 구슬은 1번 부터 n*n번 까지. 인덱스 역할도 되므로, 0을 먼저 넣기.
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))


def init(): # 칸번호와 좌표 매칭시키기, 칸번호 순서대로 구슬 번호를 marble에 할당.
    nx,ny = sx,sy
    cnt = 0
    idx = 0
    number =1
    while 0 <= nx < n and 0 <= ny < n: 
        # 좌 우 상 하. 2의 배수 때마다 이동 칸수가 하나씩 늘어남. 1 1, 2 2, ,,
        idx %= 4 # 4번째 마다 방향 순환.
        if idx %2 == 0: # 2의 배수 번째 마다, 칸수 증가
            cnt += 1
        for _ in range(cnt):
            nx += mx[idx]
            ny += my[idx]
            if 0 <= nx < n and 0 <= ny < n:
                marble.append(g[nx][ny]) # 구슬번호 할당.
                num[(nx,ny)] = number # 방향에 맞게 각 칸번호 1번 부터 n*n번까지 할당.
                number += 1
        idx += 1
def destroy():# d방향 s거리 이하까지 모두 파괴.
    global marble
    nx,ny = sx,sy
    for _ in range(s):
        nx += dx[d]
        ny += dy[d]
        number = num[(nx,ny)]
        marble[number]= -1

def move(): # 구슬 빈칸 지우고 앞쪽으로 당기기.
    global marble
    deleteCnt = marble.count(-1)

    marble = [value for value in marble if value != -1]
    
    marble.extend([0]*deleteCnt) # 당기고 남은 빈칸 채우기.

def explosion():# 연속되는 구슬 폭발.
    global marble
    flag = False
    cnt =0
    start =0 # 구슬을 없애기 위해 시작하는 인덱스를 담을 변수.
    now = marble[0]# 현재 구슬 번호.
    for i in range(n*n):
   
        if now == marble[i]:
            cnt += 1
        else:
            if cnt >= 4: # 4개이상이라면
                flag = True
                answer[now] += cnt # 파괴되는 구슬 개수 update
                for j in range(start,i): # 처음 입력은 연속되는 구슬이 없기에, 최대 6개씩.
                    marble[j] = -1
            cnt = 1 # 다시 구슬 번호를 세기 위해서, 개수와 현재 구슬 번호, 시작 인덱스 초기화
            now = marble[i]
            start = i
    return flag

def change():# 그룹화해서 변화 주기. 개수, 구슬 번호 순으로 할당.
    global marble
    new = [0]
    group = []
    for i in range(1,n*n):
        if not group:
            group.append(marble[i])
        elif group[0] == marble[i]:
            group.append(marble[i])
        else:# 번호가 달라 질 때, 지금까지 그룹 내 개수와 숫자 할당. 다음에 또 세기 위해서 group 재할당.
            new.append(len(group))
            new.append(group[0])
            group = [marble[i]]
        
    marble = [0]* (n*n) 
    for i in range(len(new)): # n*n까지만 잘라서 할당.
        if i >= n*n:
            break
        marble[i] = new[i]
    

    
init()


for _ in range(m):
    d,s = map(int,input().split())
    d -=1
    destroy()
    move()
    while explosion():
        move()
    change()

print(answer[1]+(2*answer[2]) + (3*answer[3]))