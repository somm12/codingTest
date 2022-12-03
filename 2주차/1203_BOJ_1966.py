from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append((arr[i], i))
    nth = 0
    while True:
        v = q.popleft()
        for i in q:
            if v[0] < i[0]:
                q.append(v)
                break
        else:
            nth += 1
            if v[1] == m:
                print(nth)
                break