n,m = map(int,input().split())

g= []
for _ in range(n):
    g.append(list(map(int,input().split())))
locat = {}# x,y 좌표에서의 idx값(순서) 저장.
arr = []
point = [0]*4
dx = [0,1,0,-1]
dy = [1,0,-1,0]
total = (n*n) - 1

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n
def isFinish():
    cnt = 0
    for v in arr:
        if v > 0:
            cnt += 1
    return cnt == 0

def init():# 몬스터가 이동하는 경로를 순서대로 위치 정보와, 그에 해당하는 번호 저장.
    mx = [0,1,0,-1]
    my = [-1,0,1,0]

    nx,ny = n//2,n//2
    cnt,di,idx = 0,0,0
    while inRange(nx,ny):
        if di%2 == 0:
            cnt += 1
        for _ in range(cnt):
            nx += mx[di]
            ny += my[di]
            if inRange(nx,ny):
                locat[(nx,ny)] = idx
                idx += 1
                arr.append(g[nx][ny])
        di = (di+1)%4

def attack():# 공격.
    global arr,point
    sx,sy = n//2,n//2
    for _ in range(p):
        sx += dx[d]
        sy += dy[d]
        idx = locat[(sx,sy)]
        num = arr[idx]
        if num > 0:
            point[num] += 1
            arr[idx] = 0

def org():# 중간에 빈칸을 지나 앞으로 이동.
    global arr
    tmp = []
    for v in arr:
        if v > 0:
            tmp.append(v)
    arr = tmp
    for _ in range(total-len(arr)):
        arr.append(0)

def isRepeat():# 4개이상 연속인 번호는 삭제.
    global arr,point
    cnt = 0
    start = 0
    now = arr[0]
    flag = False

    for i,v in enumerate(arr):
        if v == 0:
            break
        if now == v:
            cnt += 1
        else:
            if cnt >= 4:
                flag = True
                point[now] += cnt
                for j in range(start,i):
                    arr[j] = 0
                cnt = 1
                start = i
                now = v

            else:
                cnt = 1
                start = i
                now = v
    if cnt >= 4 and now > 0:
        point[now] += cnt
        flag = True
        for j in range(start,start+cnt):
            arr[j] = 0
        
    return flag

def makeNew():# 개수, 번호 형식으로 새로운 형태로 만드릭.
    global arr
    now = arr[0]
    cnt = 0
    tmp = []
    for v in arr:
        if v == 0:
            break
        if v == now:
            cnt += 1
        else:
            tmp.append(cnt)
            tmp.append(now)
            now = v
            cnt = 1
    if cnt > 0 and now > 0:
        tmp.append(cnt)
        tmp.append(now)
    if len(tmp) >= n*n:# 격자 밖 이상으로 길이가 길면 자르기.
        arr = tmp[:(n*n)-1]
    else:
        arr = tmp
        for _ in range(total-len(arr)):
            arr.append(0)
        
init()

for _ in range(m):
    d,p = map(int,input().split())
    if isFinish():
        break
    
    attack()

    org()

    while isRepeat():
        org()
    
    makeNew()




answer = 0
for i in range(1,4):
    answer += (i*point[i])
print(answer)