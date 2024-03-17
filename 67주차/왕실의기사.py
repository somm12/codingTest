from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

L,N,Q = map(int,input().split())

g = []
for _ in range(L):
    g.append(list(map(int,input().split())))

people= {}
demageCnt = [0]*(N+1)
locat = [[0]*L for _ in range(L)]
for i in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    r -= 1
    c -= 1
    arr = []
    for x in range(r,r+h):# 0 ~ 2
        for y in range(c,c+w):# 1 ~
            locat[x][y] = i
            arr.append((i,x,y))
    people[i] = [arr,h,w,k]


def inRange(x,y):
    return 0 <= x < L and 0 <= y < L

def move():
    global locat,people
    q = deque(people[num][0])
    result = [[] for _ in range(N+1)]# 다음 이동할 위치를 담은 배열.
    flag = False
    pushedNumbers = set()
    while q:
        number,x,y = q.popleft()
        nx,ny = x+dx[d],y+dy[d]
        if not inRange(nx,ny) or g[nx][ny] == 2:# 벽에 도달하면 모두 이동을 안함.
            return False
        result[number].append((number,nx,ny))
        if locat[nx][ny] != number and locat[nx][ny] > 0 and locat[nx][ny] not in pushedNumbers :# 충돌 발생
            flag = True
            other = locat[nx][ny]
            pushedNumbers.add(other)
            for _,a,b in people[other][0]:
                q.append((other,a,b))
    tmp = [[0]*L for _ in range(L)]
    moved = []
    newp = {}
    for i in range(1,N+1):
        if i not in people:
            continue
        _,h,w,k = people[i]
        if len(result[i]) == 0:
            # 이동을 안하는 기사라면
            newp[i] = people[i]
            for _,nx,ny in people[i][0]:
                tmp[nx][ny]= i
        else:#이동을 한다면
            newp[i] = [result[i],h,w,k]
            moved.append(i)
            for _,nx,ny in result[i]:
                tmp[nx][ny] = i
    people = newp
    locat= tmp
    return [flag, moved]

def demage(moved):
    global people, demageCnt
    for number in moved:
        if number != num:# 명령을 받은 기사는 피해 받지 않음.
            total = 0
            for _,x,y in people[number][0]:
                if g[x][y] == 1:# 함정이라면
                    total += 1
            demageCnt[number] += total
            
            if people[number][3] - total <= 0:
                for _, x,y in people[number][0]:
                    locat[x][y] = 0
                del people[number]
            else:
                people[number][3] -= total # 체력 깎임.


for nth in range(1,Q+1):
    num,d = map(int,input().split())
    if num in people:# 격자 판에 해당 기사가 있다면 이동.
        rv = move()  
        if rv != False:# 기사들이 이동을 했다면
            collision,arr = rv
           
            if collision:# 충돌이 생겼다면
                demage(arr)
              

answer = 0
for num in people:
    answer += demageCnt[num]
print(answer)
