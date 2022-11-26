n = int(input())
arr = [[0] * n for _ in range(n)]
move = list(input().split())
x = 0
y = 0
nx = x
ny = y

for i in move:
    if i == 'U':
        nx = x - 1
    elif i == 'D':
        nx = x + 1
    elif i == "L":
        ny = y - 1
    elif i == "R":
        ny = y + 1
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
    else:
        x = nx
        y = ny
print(x + 1, y + 1)