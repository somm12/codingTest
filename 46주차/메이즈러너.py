n,m,k = map(int,input().split())
g = []
people = {}
for _ in range(n):
    g.append(list(map(int,input().split())))

for i in range(m):
    x,y = map(int,input().split())
    people[i] = [x-1,y-1]
ex,ey = map(int,input().split())
ex -=1
ey -=1
answer =0
dx = [-1,1,0,0]# 상하좌우
dy = [0,0,-1,1]

def move():
    global people,answer
    tmp = {}
    for num in people:
        x,y = people[num]
        now = abs(ex-x)+abs(ey-y)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx <n and 0 <= ny < n and g[nx][ny] == 0:
                next = abs(ex-nx)+abs(ey-ny)
                if next < now:
                    answer +=1
                    if not (ex == nx and ey == ny):
                        tmp[num]= [nx,ny]
                    break
        else:# 이동 불가능.
            tmp[num]= [x,y]
    people =tmp

def check(x,y,tx,ty, length):
    return x <= tx < x+length and y <= ty < y+length
def choose():
    for length in range(2,n+1):
        for x in range(n):
            for y in range(n):
                if x + length <= n and y+length <= n:
                    for num in people:
                        i,j = people[num]
                        if check(x,y,i,j,length) and check(x,y,ex,ey,length):
                            return [x,y,length]
def rotate(i,j,length):
    global g,ex,ey,people

    flag = True# 출구 회전되었는지 여부.
    newPeople={}
    tmp = [arr[:] for arr in g]

    for x in range(length):
        for y in range(length):
            px,py = i+x,j+y
            nx,ny = y+i,length-1-x+j


            tmp[nx][ny] = g[px][py]
            if tmp[nx][ny] > 0:
                tmp[nx][ny] -= 1
            if x+i == ex and y+j == ey and flag:
                ex,ey = y+i, length-1 - x + j
                flag= False

            for num in people:
                a,b =people[num]

                if a ==px and b ==py:
                    newPeople[num] = [nx,ny]

    for num in people:#정사각형 밖의 참가자들 .
        if num not in newPeople:
            a,b = people[num]
            newPeople[num] = [a,b]

    g = tmp
    people=newPeople

for _ in range(k):

    move()

    if len(people) == 0:
        break

    a,b,length = choose()

    rotate(a,b,length)
print(answer)
print(ex+1,ey+1)

# 코드트리 기출.