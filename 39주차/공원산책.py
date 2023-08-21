def solution(park,routes):
    answer = []
    dx= [-1,1,0,0]
    dy = [0,0,-1,1]
    direction = {'N':0,'S':1, 'W':2,'E':3}# 각 방향에 대한 숫자를 담음. 이 숫자로 방향 배열인 dx,dy의 인덱스 역할을 함.
    n =len(park)# 행
    m = len(park[0])# 열
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':# 시작점인 S 찾기.
                sx,sy=i,j

    for com in routes:# 명령어 배열 에서 하나씩 방향과 몇 칸 이동할지 split하기
        d,num = com.split()
        num = int(num)
        nx,ny = sx,sy# 현재 sx,sy의 위치를 nx,ny 변수에 담고 1. 격자 범위를 벗어나지 않고, 2. 장애물을 그 동안 만나는 않는가 체크.
        for _ in range(num):
            nx += dx[direction[d]]# 해당 방향으로 이동.
            ny += dy[direction[d]]
            if 0 <= nx < n and  0<= ny < m and park[nx][ny] != 'X': # 혹시 범위를 벗어나거나, 장애물을 만나면 break 
                continue
            else:
                break
        else:# 중간에 break를 만나지 않았다면, 이동 가능 하므로, 위치 update
             sx,sy = nx,ny   
    return [sx,sy]
# 프로그래머스 문제