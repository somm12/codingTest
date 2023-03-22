def solution(dirs):
    answer = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    x = 0
    y = 0
    dict = {}
    
    direction = {'U':0,'D':1,'L':2,'R':3}
    for s in dirs:
        nx = x + dx[direction[s]]
        ny = y + dy[direction[s]]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (nx,ny,x,y) not in dict:
                dict[(x,y,nx,ny)] = 1
            x = nx
            y = ny
    answer = len(dict)
    return answer
# 방문 길이