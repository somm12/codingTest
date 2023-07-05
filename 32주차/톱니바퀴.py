from collections import deque
cycle = [0]
for _ in range(4):
    cycle.append(deque(input()))
k = int(input())

# 회전 하는 바퀴를 중심으로 오른쪽에 있는 바퀴들 회전
def rotateRight(n,d):
    if n > 4 or cycle[n][6] == cycle[n-1][2]:# 같은 극 또는 마지막 바퀴면 return
        return
    
    if cycle[n][6] != cycle[n-1][2]:# 극이 다르면 반대방향으로 회전
        rotateRight(n+1,-d)
        cycle[n].rotate(d)
# 회전 하는 바퀴를 중심으로 왼쪽에 있는 바퀴들 회전
def rotateLeft(n,d):
    if n < 1 or cycle[n][2] == cycle[n+1][6]: # 같은 극 또는 마지막 바퀴면 return
        return
    
    if cycle[n][2] != cycle[n+1][6]:# 극이 다르면 반대방향으로 회전
        rotateLeft(n-1,-d)
        cycle[n].rotate(d)

for _ in range(k):
    nth, d = map(int,input().split())
    rotateLeft(nth-1,-d) # 왼쪽에 있는 바퀴 회전
    rotateRight(nth+1,-d) # 오른쪽에 있는 바퀴 회전
    cycle[nth].rotate(d) # 고른 바퀴 회전.
    
answer = 0

for i in range(1,5):
    answer += int(cycle[i][0]) * (2**(i-1))# 점수 계산
print(answer)