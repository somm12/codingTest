n = int(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]
every = []
def count(arr):
    total = 0
    arr = list(set(arr))
    for x,y in arr:
        cnt = 0
        for i,j in [(0,-1),(1,-1),(1,0)]:
            if (x+i, y+j) in arr:
                cnt += 1
        if cnt == 3:
            total += 1
    return total
for _ in range(n):
    x,y,d,g = map(int,input().split())
    points = []
    points.append((x,y))
    nx = x + dx[d]
    ny = y + dy[d]
    points.append((nx,ny))
    # 1세대 이상 만들기
    for _ in range(1, g+1):
        a,b = points[-1]# 현재 세대에서 기준점
        t = len(points) - 1
        for i in range(t-1,-1,-1):
            pre_x, pre_y = points[i]
            diff_x, diff_y = a - pre_x, b - pre_y
            if pre_x == a:
                points.append((a+diff_y,b+diff_x))
            else:
                points.append((a+diff_y,b-diff_x))
    for i,j in points:
        every.append((i,j))
print(count(every))
        