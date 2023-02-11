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
    
edges = []
x = []
y = []
z = []

n = int(input())
for i in range(1,n+1):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i+1][1],x[i][1]))
    edges.append((y[i+1][0] - y[i][0], y[i+1][1],y[i][1]))
    edges.append((z[i+1][0] - z[i][0], z[i+1][1],z[i][1]))
edges.sort()
result = 0
parent = [i for i in range(n+1)]
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        result += cost
        union(parent,a,b)
print(result)