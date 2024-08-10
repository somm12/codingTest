
n,m,k = map(int,input().split())
A= []
tree = [[[] for _ in range(n)] for _ in range(n)]

food= [[5]*n for _ in range(n)]
for _ in range(n):
    A.append(list(map(int,input().split())))
    
for _ in range(m):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def spring():
    global food,tree
    
    for x in range(n):
        for y in range(n):
            
            tree[x][y].sort()
            tmp = []
            nxtFood= 0
            for age in tree[x][y]:
                if food[x][y] >= age:
                    food[x][y] -= age
                    tmp.append(age+1)
                else:#죽음
                    nxtFood += (age//2)
            food[x][y] += nxtFood
            tree[x][y] = tmp
            

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def fall():
    global tree
    tmp = []
    for x in range(n):
        for y in range(n):
            for age in tree[x][y]:
                if age %5 == 0:
                    for i in range(8):
                        nx,ny = x+dx[i],y+dy[i]
                        if inRange(nx,ny):# 나무 심을 위치.
                            tmp.append((nx,ny))
            food[x][y] += A[x][y]
    for x,y in tmp:
        tree[x][y].append(1)   
            
        
for _ in range(k):
    spring()
    fall()

answer = 0
for x in range(n):
    for y in range(n):
        answer+= len(tree[x][y])
print(answer)