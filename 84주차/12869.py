from collections import deque
n =int(input())
tmp = [[9,3,1],[9,1,3],[3,9,1],[3,1,9],[1,9,3],[1,3,9]]# 최대 6가지 경우.

arr = [0]*3
for i,v in enumerate(list(map(int,input().split()))):# n이 3개라고 치고, 임의의로 0으로 모두 할당 후, 값 할당.
    arr[i] = v
visited = [[[0]*61 for _ in range(61)] for _ in range(61)]# 각 숫자에 따른 횟수 저장 배열.

def bfs(a,b,c):
    q = deque()
    q.append((a,b,c))
    visited[a][b][c] = 1 # 방문처리는 1이상의 수로 처리 겸 횟수 저장. => 마지막에 -1 해주기.
    while q:
        a,b,c = q.popleft()
        if visited[0][0][0]:# 모두 제거 되었다면 break
            break
        for i in range(6):
            na = max(0, a - tmp[i][0])
            nb = max(0, b - tmp[i][1])
            nc = max(0, c - tmp[i][2])
            if visited[na][nb][nc]:
                continue
            visited[na][nb][nc] = visited[a][b][c] + 1
            q.append((na,nb,nc))
    return visited[0][0][0] - 1

print(bfs(arr[0],arr[1],arr[2]))
# bfs 최단거리 방식을 이용해서 불필요한 탐색을 걷어내기. 이미 방문한 부분은 넘김.
# 백준 뮤탈리스크