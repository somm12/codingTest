n,m,h,k= map(int,input().split())
people = {}
dx = [-1,0,1,0]# 상 우 하 좌
dy = [0,1,0,-1]

for i in range(1,m+1):
    x,y,d = map(int,input().split())
  
    people[i] = [x-1,y-1,d]
   
tree= [[0]*n for _ in range(n)]
for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1
# 도망자 패턴 위치, 현재 위치, 현재 방향
cidx=0
cx,cy = n//2,n//2
cd = 0
#
answer = 0

pattern = []

def init():# 술래의 이동 패턴 구하기.
    global pattern
    x,y = cx,cy
    di = 0
    cnt = 0
    arr1,arr2= [],[]
    while 0 <= x < n and 0 <= y < n:
        if di%2 == 0:
            cnt += 1
        for _ in range(cnt):
            if inRange(x,y):
                arr1.append([x,y,di])
            
            x += dx[di]
            y += dy[di]
        di = (di+1)%4
    
    for i in range(len(arr1)-1,0,-1):
        x,y,di = arr1[i]
        nx,ny,nd = arr1[i-1]
        arr2.append((x,y,(nd+2)%4))
    pattern = arr1[:-1] + arr2


init()

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def runnerMove():
    global people
    tmp = {}
    for num in people:
        x,y,di = people[num]
        if abs(x- cx) + abs(y-cy) <= 3:# 술래와 거리가 3이하인 도망자만 이동.
            nx,ny = x+dx[di],y+dy[di]
            if inRange(nx,ny):
                if nx == cx and ny == cy:
                    tmp[num] = [x,y,di]
                else:
                    tmp[num] = [nx,ny,di]
            else:
                nd = (di+2)%4
                nx,ny = x+dx[nd],y+dy[nd]
                if nx == cx and ny == cy:
                    tmp[num] = [x,y,nd]
                else:
                    tmp[num] = [nx,ny,nd]
        else:
            tmp[num] = [x,y,di]
    people = tmp

def catcherMove():
    global cidx,cx,cy,cd
    cidx = (cidx+1)% len(pattern)
    cx,cy,cd = pattern[cidx]

def catchRunner():
    global answer,people
    scope= set()
    tmp = {}
    x,y =cx,cy
    for _ in range(3):
        if inRange(x,y):
            scope.add((x,y))
        x += dx[cd]
        y += dy[cd]
    cnt = 0
    for num in people:# 3칸 시야 이내에서, 나무에 숨지 않은 도망자는 잡힘.
        x,y,di = people[num]
        if (x,y) in scope and tree[x][y] == 0:# 잡힘.
            cnt += 1
        else:
            tmp[num] = [x,y,di]
    people = tmp
    answer += (nth*cnt)# 점수 획득

for nth in range(1,k+1):
    if len(people) == 0:
        break
    runnerMove()
    
    catcherMove()
    catchRunner()
print(answer)
