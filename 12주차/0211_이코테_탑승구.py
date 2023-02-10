import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

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

parent = [i for i in range(g+1)]
res = 0
for _ in range(p):
    data = find_parent(parent,int(input()))
    if data == 0:
        break
    union(parent,data,data-1)
    res += 1
print(res)
