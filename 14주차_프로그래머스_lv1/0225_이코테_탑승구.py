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

cnt = 0
n = int(input())
parent = [i for i in range(n+1)]
p = int(input())
plane = []
for _ in range(p):
    plane.append(int(input()))

for g in plane:
    a = find_parent(parent,g)
    if a == 0:
        break
    union(parent,a-1,a)
    cnt += 1
print(cnt)