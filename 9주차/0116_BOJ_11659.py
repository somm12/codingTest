import sys
input = sys.stdin.readline
n, m = map(int, input().split())
p = [0]
arr = list(map(int, input().split()))
val = 0
for i in arr:
    val += i
    p.append(val)

for _ in range(m):
    s,e = map(int, input().split())
    print(p[e]-p[s-1])