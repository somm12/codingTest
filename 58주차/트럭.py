from collections import deque

n,W,L = map(int,input().split())
q = list(map(int,input().split()))
q = deque(q)

bridge = deque([0]*W)
total = 0
t = 0
while q or total > 0:
    v = bridge.popleft()
    if v > 0:# 1칸 건넌 뒤, 다리 위에 있던 트럭 무게 값 빼기
        total -= v
    
    if q and total + q[0] <= L:# 최대 하중 이하라면 다리에 올라감.
        truck = q.popleft()
        bridge.append(truck)
        total += truck
    else:# 최대하중 초과를 하게 되면, 다리에 있던 트럭들만 이동함.(0을 추가해서 이를 표현.)
        bridge.append(0)
    t += 1
    
print(t)