def solution(park, routes):
    answer = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dict = {'N':0,'S':1,'W':2,'E':3}
    n = len(park)
    m = len(park[0])
    flag = False
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                rx,ry = i,j
                flag = True
                break
        if flag:
            break
    
    for com in routes:
        d,s = com.split(" ")
        s = int(s)
        nx,ny = rx,ry
        for _ in range(s):
            nx += dx[dict[d]]
            ny += dy[dict[d]]
            # O, S 두 곳 모두 방문 가능.
            if 0 <= nx < n and 0 <= ny < m and park[nx][ny] !='X':
                continue
            else:
                break
        else:
            rx,ry = nx,ny
    
        
    return [rx,ry]
# 프로그래머스. 