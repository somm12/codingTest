from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        if board[i][j] == 'X':
            spaces.append((i,j))

def watch(x,y,direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    if direction == 3:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    return False
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False
ans = False
for c in combinations(spaces,3):
    for x, y in c:
        board[x][y] = 'O'
    if not process():# 발견 못했다면,
        ans = True
        break
    for x,y in c:
        board[x][y] = 'X'

if ans:
    print("YES")
else:
    print("NO")