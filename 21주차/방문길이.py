def solution(dirs):
    answer= 0
    dict = {'U': (0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
    visited = {}
    x,y= 0,0
  
    for i in dirs:
        nx = x+dict[i][0]
        ny = y + dict[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (nx,ny,x,y) not in visited:
                visited[(x,y,nx,ny)] = 1
            x = nx
            y = ny
    print(visited)
    answer = len(visited)
    return answer