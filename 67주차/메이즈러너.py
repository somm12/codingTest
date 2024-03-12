n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

people = {}
for i in range(1,m+1):
    x,y = map(int,input().split())
    people[i] = [x-1,y-1]
ex,ey = map(int,input().split())
ex -= 1
ey -= 1

dx = [-1,1,0,0]
dy =[0,0,-1,1]
answer = 0

def inRange(x,y):
    return 0 <= x< n and 0<= y < n

def move():
    global people, answer
    tmp = {}
    for num in people:
        x,y = people[num]
        isMoved = False
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny)and g[nx][ny] == 0:
                nd = abs(nx - ex) +abs(ny-ey)
                d = abs(x - ex) + abs(y - ey)
                if nd < d:
                    isMoved = True
                    if not (nx == ex and ny == ey):# 탈출구가 아니라면 이동함, 탈출구면 즉시 탈출.
                        tmp[num] = [nx,ny]
                    break
        if not isMoved:
            tmp[num] = [x,y]
        else:# 이동을 했다면
            answer += 1
    people = tmp

def check(length, x,y):
    cnt = 0
    isExit = False
    for num in people:
        px,py = people[num]
        if x <= px < x+length and y <= py < y+length:
            cnt += 1
            break
    if x <= ex < x+length and y <= ey < y+ length:
        isExit = True
    
    if cnt > 0 and isExit:
        return True
    return False

def rotate():
    global people, ex,ey, g
    tmp = {}
    newG =[ arr[:] for arr in g ]
   
    isExit = True
    for x in range(length):
        for y in range(length):
            px,py = tx+x,ty+y
            nx,ny = tx+y, ty+length - 1 - x
            
            if g[px][py] > 0:
                newG[nx][ny] = g[px][py] - 1
            else:
                newG[nx][ny] = g[px][py]
            if isExit and px == ex and py == ey:
                ex,ey = nx,ny
                isExit = False
            
            for num in people:
                prevX,prevY = people[num]
                if prevX == px and prevY == py:
                    tmp[num] = [nx,ny]
    
    for num in people:
        x,y = people[num]
        if num not in tmp:
            tmp[num] = [x,y]

    people = tmp
    g = newG

def find():
    for length in range(2,n+1):
        for x in range(0,n):
            for y in range(0,n):
                if x+length <= n and y+length <= n and check(length,x,y):
                    return [x,y,length]
            
for t in range(1,k+1):
      
    move()

    if len(people) == 0:
        break
    tx,ty,length = find()
  
    rotate()


print(answer)
print(ex+1,ey+1)
