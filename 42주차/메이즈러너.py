import copy
n,m,k = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
people = {}
for i in range(1,m+1):
    a,b= map(int,input().split())
    people[i] = [a-1,b-1]
ex,ey = map(int,input().split())
ex -= 1
ey -=1

total = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move():
    global people, total
    newPeople = {}
    for p in people:
        x,y = people[p]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] ==0:
                
                if abs(nx-ex)+abs(ny-ey) < abs(x-ex)+abs(y-ey):
                    total += 1
                    if not (nx == ex and ny == ey):
                        newPeople[p] = [nx,ny]
                    break
        else:# 이동 불가하면 그대로.
            newPeople[p] = [x,y]
    people = newPeople


def makeSquare():
    
    for length in range(2,n+1):
        for i in range(n):
            for j in range(n):
                    if i+length <= n and j+length <= n:
                        for p in people:
                            x,y = people[p]
                            if i <= x <i+length and j <= y <j + length:
                                if i <= ex <i+length and j <= ey <j + length:
                                    return [i,j,length]
    

def rotate(x,y,length):
    global g,people,ex,ey

    tmp = copy.deepcopy(g)
    newPeople = {}
    flag = False
    for i in range(length):
        for j in range(length):
            px,py = i+x,j+y 
            nx,ny = j+x,length-1-i+y
            tmp[nx][ny] = g[px][py]
            if tmp[nx][ny] > 0:
                tmp[nx][ny] -= 1
            for p in people:
                a,b = people[p]
                if a==px and b == py:
                    newPeople[p] = [nx,ny]
            
            if not flag and ex == px and ey == py:
                ex,ey = nx,ny
                flag = True
    for p in people:# 정사각형 내에 해당하지 않는 참가자 옮기기.
        a,b = people[p]
        if not (x <= a < x+length and y <= b < y+length):
            newPeople[p] = [a,b]
      
    g = tmp
    people = newPeople


for t in range(1,k+1):

    move()
    if len(people) == 0: # 이전에 모두가 탈출해서 끝난다면 break
        break
    x,y,length = makeSquare() # 가장 작은 정사각형 찾기
    rotate(x,y,length)# 회전하기.
    
    
print(total)
print(ex+1,ey+1)
# 회전 부분.
# move 뒤에 break 조건.