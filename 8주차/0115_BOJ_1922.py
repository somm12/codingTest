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
n = int(input().rstrip())
m = int(input().rstrip())
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()
result = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        result += cost

print(result)