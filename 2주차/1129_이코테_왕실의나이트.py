a = input()
dx = [-1,-2,-2,-1,1,1,2,2]
dy = [-2,-1,1,2,-2,2,-1,1]
x = int(a[1]) - 1
y = ord(a[0]) - 97
cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        continue
    cnt += 1
print(cnt)

# steps = [(-2,-1), (-1,-2), (1,-2), (-2,1) (-1,2), (2,-1), (1,2), (2,1)]로도 가능.