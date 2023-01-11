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

T = int(input().rstrip())
for _ in range(T):
    n, m = map(int, input().split())
    edges = []
    parent = [i for i in range(n+1)]
    result = 0
    for _ in range(m):
        a,b = map(int, input().split())
        edges.append((a,b,1))
    for edge in edges:
        a,b,cost = edge
        if find_parent(parent,a) != find_parent(parent,b):
            result += cost
            union(parent,a,b)
    print(result)