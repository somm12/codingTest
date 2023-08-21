n,m = map(int,input().split())
sx,sy,d = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
turn = 0# 현재까지 회전한 횟수
answer = 0# 개수 세기
visited = [[0]*m for _ in range(n)]# 방문처리

while True:
   
    d -= 1# 왼쪽으로 회전
    d %=4
    nx = sx+dx[d]
    ny = sy+dy[d]

    if g[nx][ny] == 0 and not visited[nx][ny]:# 방문하지 않은 칸이라면
        sx,sy = nx,ny# 전진하기
        visited[nx][ny] = 1# 방문처리
        answer += 1# 개수 세기
        turn = 0# 다시 회전한 횟수 리셋.
    else:# 바다나 이미 방문한 칸이라면
        turn += 1# 회전만 하기.
        if turn == 4: # 만약 4방향 모두 방문한 칸 or 바다면
            nx = sx-dx[d]# 현재 방향 유지한 채로! 후진.
            ny = sy-dy[d]
            turn = 0 # 다시 회전 횟수 리셋.
            if g[nx][ny] == 1:# 하지만 후진 방향에 바다가 있다면 break
               
                break
            sx,sy = nx,ny # 한칸 뒤로 후진.

print(answer)
# 현재 방향을 유지한채로 후진하는 연산에 유의
# 이코테 실전연습 복습.