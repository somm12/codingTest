n= int(input())

stud = [[] for _ in range(n*n+1)]

g = [[0]*(n) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <= x< n and 0 <=y < n

def choose(num):
    global g
    cand = []
   
    for x in range(n):
        for y in range(n):
            if g[x][y] != 0: continue# 이미 정해진 자리는 패스.
            empty = 0
            like =0
            for i in range(4):# 인접 4칸.
                nx,ny = x+dx[i],y+dy[i]
                if inRange(nx,ny):
                    if g[nx][ny] == 0:# 빈자리 세기
                        empty+= 1
                    elif g[nx][ny] in stud[num]:# 좋아하는 학생이 있는지 세기.
                        like += 1
            cand.append((like,empty, x,y))
    cand.sort(key= lambda x:(-x[0],-x[1],x[2],x[3]))# 좋아하는 학생 수 > 빈자리 > 행이작고 > 열이 작고.
    tx,ty = cand[0][2],cand[0][3]
    g[tx][ty] = num

def cal():# 만족도 계산.
    global answer
    for x in range(n):
        for y in range(n):
            cnt = 0
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if inRange(nx,ny):
                    if g[nx][ny] in stud[g[x][y]]:
                        cnt += 1
            if cnt > 0:
                answer += (10 **(cnt-1))
                
for _ in range(n*n):
    arr = list(map(int,input().split()))
    stud[arr[0]] = arr[1:]
    choose(arr[0])

answer = 0
cal()
print(answer)
# 백준 상어 초등학교

    