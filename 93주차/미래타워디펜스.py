dx = [0,1,0,-1]
dy = [1,0,-1,0]
n,m = map(int,input().split())
L = n*n -1
g = []

at = []# 공격 정보.
for _ in range(n):
    g.append(list(map(int,input().split())))

for _ in range(m):
    at.append(list(map(int,input().split())))
answer = 0
info = {}

def inRange(x,y):
    return 0 <= x< n and 0 <= y < n
def init():
    mx = [0,1,0,-1]
    my = [-1,0,1,0]
    tmp =[]
    cnt = 0
    di = 0
    num = 0
    x,y = n//2,n//2
    while inRange(x,y):
        if di % 2 == 0:
            cnt += 1
        for _ in range(cnt):
            x += mx[di]
            y += my[di]
            if inRange(x,y):
                tmp.append(g[x][y])
                info[(x,y)]= num
                num += 1
        di = (di+1)%4
    return tmp

def attack():
    global arr,answer
    sx,sy = n//2,n//2
    point = [0]*4
    for _ in range(p):
        sx += dx[d]
        sy += dy[d]
        idx = info[(sx,sy)]
        v = arr[idx]
        arr[idx] = 0
        point[v] += 1
    for i in range(1,4):
        answer += (i*point[i])

def go():
    global arr
    tmp = []
    for v in arr:
        if v != 0:
            tmp.append(v)
    for _ in range(L-len(tmp)):
        tmp.append(0)
    arr = tmp

def check():
    global arr,answer
    flag = False
    start =0
    cnt = 0
    prev = arr[0]
    for i in range(L):
        if arr[i] == 0: break
        if arr[i] == prev:
            cnt += 1
        else:
            if cnt >= 4:
                answer += (prev*cnt)
                for idx in range(start,i):
                    arr[idx] = 0
                flag= True
            prev = arr[i]
            cnt = 1
            start = i

    if cnt >= 4:
        for i in range(start,start+cnt):
            arr[i] = 0
        answer += (prev*cnt)
        flag= True
    return flag

def put():
    global arr
    tmp = []
    cnt = 0
    prev = arr[0]
    for i in range(L):
        if arr[i] == 0: break
        if arr[i] == prev:
            cnt += 1
        else:
            tmp.append(cnt)
            tmp.append(prev)
            prev = arr[i]
            cnt = 1
    tmp.append(cnt)
    tmp.append(prev)
    if len(tmp) > L:
        tmp = tmp[:L]
    else:
        for _ in range(L-len(tmp)):
            tmp.append(0)
    arr = tmp



arr = init()

for d,p in at:
    attack()
    go()
    while check():
        go()
    put()

print(answer)
# 코드트리 문제. 
# 나선형은 하나의 배열을 만들어서 풀자.