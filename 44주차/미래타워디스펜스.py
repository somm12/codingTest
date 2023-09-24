n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

sx,sy = n//2,n//2# 중심 좌표. 가운데.
num = [[0]*n for _ in range(n)]# 각 좌표에서의 monster 배열의 인덱스를 담을 배열.
answer = [0,0,0] # 1,2,3 번 몬스터 각각 제거된 개수를 담을 배열.
monster =[]
dx = [0,1,0,-1]# d,p를 입력 받을 때, 방향대로 지정(우 하 좌 상)
dy = [1,0,-1,0]
# 달팽이 모양 대로 중심부터 (0,0)좌표 까지 방향을 순서대로 나타낸 배열. 좌 하 우 상 
mx = [0,1,0,-1]
my = [-1,0,1,0]

# num[x][y]는 monster의 인덱스 역할을 함.
def init():# 입력 받은 배열을 일자로 뒀을 때 모양을 monster에 할당하기, num 배열에 각 좌표에서 monster의 인덱스를 할당.
    global monster,num
    x,y=n//2,n//2
    cnt = 0
    di = 0
    idx = 0
    while 0<=x <n and 0<=y < n:# 범위를 벗어나면 종료.
        if di % 2 == 0:# 1 1 2 2 3 3 ,, (몇 칸씩 좌 하 우 상 방향 대로 나아감.) 방향이 짝수 인덱스 일 때, cnt 증가.
            cnt += 1
        for _ in range(cnt):
            x += mx[di]
            y += my[di]
            if 0 <= x <n and 0 <= y < n:
                monster.append(g[x][y])
                num[x][y] = idx # 인덱스 할당.
                idx +=1 
            else:
                break
        di = (di+1)%4

def remove():# d방향 p칸 만큼 제거.
    global monster, answer
    x,y = sx,sy
    for _ in range(p):
        x += dx[d]
        y += dy[d]
        if 0 <= x < n and 0 <= y < n:
            idx = num[x][y]
            v = monster[idx]
            monster[idx] = 0
            if v > 0:# ***** 만약 해당 칸의 값이 0이라면, 점수에 해당 하지 않는 부분(1,2,3만 구함) 이므로 유의해야함.*****
                answer[v-1] += 1
        else:
            break
def org():# 비워진 부분 제외하고 다시 새로 배열을 만든다. (비워진 부분을 앞으로 당긴다.)
    global monster
    tmp = []
    length = len(monster)
    for v in monster:
        if v!=0:
            tmp.append(v)
    tmp.extend([0]*(length-len(tmp)))
    monster = tmp

def sameRemove():# 연속 4개이상이면 없애기.
    global monster, answer
    flag = False
    cnt= 0
    prev = monster[0]
    start = 0
    for i in range(len(monster)):
        if monster[i]==0:# 0은 제외!**
            break
        if prev == monster[i]:
            cnt += 1
        else:
            if cnt >=4:
                flag = True
                answer[prev-1] += cnt
                for j in range(start,i):# 연속적인 부분은 0으로 할당.
                    monster[j] = 0
            start = i# 다음 연속 부분의 시작 인덱스를 담기.
            cnt = 1# 개수 세기 다시 1로.
            prev=monster[i]# 현재 비교하고자 하는 숫자 할당.
    if cnt >=4:
        flag = True
        answer[prev-1] += cnt
        for j in range(start,len(monster)):
            monster[j] = 0
    return flag

def change():# 그룹화 하기 ( 개수, 숫자 크기)형식. 만약 격자범위를 넘으면 자르기.
    global monster
    tmp = []
    prev = monster[0]
    cnt = 0
    for i in range(len(monster)):
        if monster[i] == prev:
            cnt += 1
        else:
            tmp.append(cnt)
            tmp.append(prev)
            cnt = 1
            prev = monster[i]
            if monster[i] ==0:# 0이라면 더이상 세지 않아도 됨.
                break
    else:
        tmp.append(cnt)
        tmp.append(prev)
    if len(tmp) >= n*n:# 범위 넘어서면 자르기.
        monster =tmp[:len(monster)]
    else:# 부족한 0부분 채우기.
        tmp.extend([0]*(len(monster)- len(tmp)))
        monster = tmp

init()# 초기화

for i in range(1,m+1):
    d,p = map(int,input().split())
    remove()# p칸만큼, d방향으로 삭제
    org()# 앞으로 댕기기

    while sameRemove():# 4개이상 같으면 제거

        org()# 다시 앞으로 당기기
    change()# 개수, 숫자 크기 형태로 그룹화하기.
point = 0
for i,v in enumerate(answer):
    point += ((i+1)*v)
print(point)
# 삼성 기출 코드트리.