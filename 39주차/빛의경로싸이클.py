def solution(grid):
    answer =[]
    n = len(grid)
    m = len(grid[0])
    visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
    dx = [-1,0,1,0]# 상 우 하 좌 (빛이 쏴지는 방향 기준 왼쪽으로 가면 -1, 오른쪽으로 가면 +1 방향대로.)
    dy = [0,1,0,-1]
    for x in range(n):# 각 좌표에 상 하 좌 우로 빛을 쏘았을 때.
        for y in range(m):
            for d in range(4):
                if not visited[x][y][d]:# 이미 방문했던 방향은 패스.
                    cnt = 0# 싸이클 경로 길이 세기.
                    nx,ny=x,y# 시작점.
                    while not visited[nx][ny][d]:# 다시 방문했던 점을 만나기 전까지.
                        visited[nx][ny][d] =1# 방문처리
                        cnt += 1# 개수세기.
                        
                        if grid[nx][ny] == 'L':
                            d = (d-1)%4
                        elif grid[nx][ny] == 'R':
                            d = (d+1)%4
                        nx += dx[d]# 좌표에 적힌 해당 방향으로 이동
                        ny += dy[d]
                        nx %=n# 격자 범위를 벗어나도 이어지기 때문에 행 길이로 나눠줌.
                        ny %=m# 똑같이 범위를 벗어나면 열 길이로 나눠줌.
                    answer.append(cnt)# 한 사이클이 끝나면 길이 append
    answer.sort()# 오름 차순 정렬.
    return answer
# 프로그래머스 문제.