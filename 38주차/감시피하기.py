
n = int(input())
g = []
wall = []
teacher = []

answer = 'NO'
dx = [-1,1,0,0]
dy = [0,0,-1,1]

done = False

for i in range(n):
    g.append(list(input().split()))
    for j in range(n):
        if g[i][j] == 'X':# 장애물을 설치 할 수 있는 빈 칸 후보들 추가.
            wall.append((i,j))
        elif g[i][j] == 'T':# 선생님 위치를 담음.
            teacher.append((i,j))

def avoid():# 피할 수 있는지 true or false 반환.
    global answer
    for x,y in teacher:
        for i in range(4):
            nx,ny = x,y
            while True:
                nx +=dx[i]
                ny +=dy[i]
                if 0 <= nx < n and 0 <= ny < n:# 장애물이나 범위를 벗어나면 그만, 학생을 만나면 피하기 실패.
                    if g[nx][ny] == 'O':
                        break
                    elif g[nx][ny] == 'S':
                        return False
                else:
                    break
    answer = 'YES'
    return True

def choose(L,start):# 장애물 세 개 설치.
    global g, done
    if done:
        return
    if L == 3:
        if avoid():
            done = True# 만약 이미 피할 수 있는 경우가 존재하면 true를 할당!. 이후 일은 종료시킴.
        return
    for i in range(start,len(wall)):
        x,y = wall[i]
        g[x][y] = 'O'
        choose(L+1,i+1)
        g[x][y] = 'X'
    
choose(0,0)
print(answer)
# 이코테 문제 - 백준 문제.