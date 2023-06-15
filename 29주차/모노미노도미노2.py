def checkBlue(): #파란색 보드에서 한 열이 모두 다 차있는지 체크하고 제거
    global ans
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if b[i][j]:
                cnt += 1

        if cnt == 4: # 다 차있다면, 해당 열은 제거.
            removeBlue(j)
            ans += 1 # 점수 +1 획득


def checkGreen():#초록색 보드에서 한 행이 모두 다 차있는지 체크하고 제거
    global ans
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if g[i][j]:
                cnt += 1

        if cnt == 4: # 다 차있으면, 해당 행은 제거.
            removeGreen(i)
            ans += 1 # +1 점수 획득.


def removeBlue(idx): # idx 열을 제거.
    for j in range(idx, 0, -1): # 해당 열 이전 열 모두 한칸씩 오른쪽이동.
        for i in range(4):
            b[i][j] = b[i][j-1]
    for i in range(4):# 남은 젤 왼쪽 칸은 0으로 할당
        b[i][0] = 0 


def removeGreen(idx): # 해당 행 이전 행 모두 아래로 이동.
    for i in range(idx, 0, -1):
        for j in range(4):
            g[i][j] = g[i-1][j]
    for j in range(4): # 남은 젤 위쪽 행은 모두 0 으로 할당.
        g[0][j] = 0


def moveBlue(t, x): #파란색에 블록을 옮기는 함수
    global b
    y = 1
    if t == 1 or t == 2: #1*1 or 1*2 블록
        while True:
            if y + 1 > 5 or b[x][y+1]:
                b[x][y] = 1
                if t == 2:
                    b[x][y-1] = 1
                break
            y += 1

    else:
        while True:#2*1블록
            if y + 1 > 5 or b[x][y+1] != 0 or b[x+1][y+1] != 0:
                b[x][y], b[x+1][y] = 1, 1
                break
            y += 1

    checkBlue() # 이동 후에, 한 열이 다 차있는지 체크하고, 해당 열을 지운다.

    for j in range(2):# 연한 색 블록의 열이 존재하면 바로 그 열은 제거.
        for i in range(4):
            if b[i][j]:
                removeBlue(5)
                break


def moveGreen(t, y):
    global g
    x = 1
    if t == 1 or t == 3:#1*1 or 2*1 블록 일때.
        while True:
            if x + 1 > 5 or g[x+1][y]:
                g[x][y] = 1
                if t == 3:
                    g[x-1][y] = 1
                break
            x += 1

    else: #1*2블록 일 때,
        while True:
            if x + 1 > 5 or g[x+1][y] or g[x+1][y+1]:
                g[x][y], g[x][y+1] = 1, 1
                break
            x += 1

    checkGreen() # 이동 후에, 한 행이 다 차있는지 체크하고, 해당 행을 지운다.

    for i in range(2):# 연한 색 블록의 행이 존재하면 바로 그 열은 제거.
        for j in range(4):
            if g[i][j]:
                removeGreen(5)
                break


tc = int(input())
b = [[0] * 6 for _ in range(4)] # 초록 보드
g = [[0] * 4 for _ in range(6)] # 파란 보드

ans = 0
for i in range(tc):
    t, x, y = map(int, input().split())
    moveBlue(t, x)
    moveGreen(t, y)

cnt = 0
# 총 초록보드와, 파란보드에 있는 블록 개수 구하기.
for i in range(4):
    for j in range(2, 6):
        if b[i][j]:
            cnt += 1
for i in range(2, 6):
    for j in range(4):
        if g[i][j]:
            cnt += 1

print(ans)
print(cnt)