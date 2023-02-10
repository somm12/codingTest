from functools import total_ordering
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
edges = []
for _ in range(m):
    x,y,z = map(int,input().split())
    edges.append((z,x,y))
edges.sort()
parent = [i for i in range(n+1)]

total = 0
answer = 0
for edge in edges:
    cost,a,b = edge
    total += cost
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        answer += cost
print(total-answer)

