n = int(input())
g = [[0]*n for _ in range(n)]
dict= {}
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move(num):
    global g
    cand = []
    for x in range(n):
        for y in range(n):
            if g[x][y] > 0: continue# 이미 탑승한 칸은 제외.

            empty, like = 0,0# 인접한 곳 중 좋아하는 사람 수, 빈 칸 수 세기.
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if inRange(nx,ny):
                    if g[nx][ny] in dict[num]:
                        like += 1
                    elif g[nx][ny] == 0:
                        empty += 1
            cand.append((like,empty,x,y))
    cand.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))# 좋아하는 사람수 > 빈 칸 수 > 행이 작고 > 열이 작은 우선순위.
    x,y = cand[0][2],cand[0][3]
    g[x][y] = num

for _ in range(n*n):
    arr = list(map(int,input().split()))
    dict[arr[0]] = arr[1:]
    move(arr[0])


answer = 0
# 점수 합산.
for x in range(n):
    for y in range(n):
        num = g[x][y]
        cnt = 0
        for i in range(4):
            nx= x+dx[i]
            ny = y + dy[i]
            if inRange(nx,ny) and g[nx][ny] in dict[num]:
                cnt += 1
        answer += int(10**(cnt - 1))
print(answer)