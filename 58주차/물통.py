from collections import deque
a,b,c = map(int,input().split())

q = deque()
q.append((0,0))
visited = [[0]*(b+1) for _ in range(a+1)]
visited[0][0]= 1
answer = []
def pour(x,y):
    if not visited[x][y]:
        visited[x][y] =1
        q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()
        z = c - x - y
        
        if x == 0:
            answer.append(z)
        # x->y
        water = min(x,b-y)
        pour(x-water,y+water)
        # x->z
        water = min(x,c-z)
        pour(x-water,y)
        # y->z
        water = min(y,c-z)
        pour(x,y-water)
        # y->x
        water = min(y,a-x)
        pour(x+water,y-water)
        # z->x
        water = min(a-x,z)
        pour(x+water,y)
        # z->y
        water = min(b-y,z)
        pour(x,y+water)

        
bfs()
answer.sort()
for v in answer:
    print(v,end =' ')
# a비커가 비었을 때의 c 비커에 있는 물의 양 모든 경우 찾기.

# 1. 물을 옮길 수 있는 모든 경우 찾기.(한쪽이 빌 때까지 or 한쪽이 다 찰때까지)
# => 6가지의 경우
# ** c 비커의 물의 양은 항상 c - x-y(x,y는 각 a,b 비커에 담긴 현재 물의 양.)
# 2. q에 각각 x,y 현재 물의 양을 저장하면서, 가능한 모든 경우를 answer에 넣기
# ** 이미 했던 경우를 제외하기 위해 visited 이용.