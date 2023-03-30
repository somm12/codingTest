n,m = map(int,input().split())
graph = []
comm = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
for _ in range(m):
    comm.append(list(map(int,input().split())))
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

check= [2,4,6,8]

cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
visited = [[0]*n for _ in range(n)]
for i,s in comm:
    # 구름 이동 시키기
    for idx in range(len(cloud)):
        cloud[idx][0] = cloud[idx][0] + (dx[i]*s)
        cloud[idx][1] = cloud[idx][1] + (dy[i]*s)
    for idx in range(len(cloud)):# 경계 넘었을 때 
        cloud[idx][0] = cloud[idx][0] % n
        cloud[idx][1] = cloud[idx][1] % n
        
    # 비 내림
    for x,y in cloud:
        graph[x][y] += 1
    # 대각선 확인
    for x,y in cloud:
        for d in check:
            if 0 <= x+dx[d] < n and 0 <= y+dy[d] < n:
                if graph[x+dx[d]][y+dy[d]] > 0:
                    graph[x][y] += 1
    # 구름 방문 처리
    for x,y in cloud:
        visited[x][y] = 1
    # 구름 새로 생기기 
    new = []
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                if graph[x][y] >= 2:
                    new.append([x,y])
                    graph[x][y] -= 2
    # 구름 방문 처리 다시 되돌리기
    for x,y in cloud:
        visited[x][y] = 0
    # 새로운 구름 업데이트
    cloud = new.copy()

answer = 0
for x in range(n):
    for y in range(n):
        answer += graph[x][y]
print(answer)