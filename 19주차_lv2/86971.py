from collections import Counter
def find(parent,x):
    if parent[x] !=x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] =b 

def solution(n, wires):
    answer = int(1e9)
    check = [0]*len(wires)
    for j in range(len(wires)):
        check[j] = 1
        parent=[k for k in range(n+1)]
        for i in range(len(wires)):
            if not check[i]:
                union(parent,wires[i][0],wires[i][1])
        
        uf = []
        for i in range(1, n + 1):
            uf.append(find(parent, i))
        p = Counter(uf)
        arr = list(p.values())
        answer = min(answer,abs(arr[0]-arr[1]))
        check[j] = 0
    return answer

# 전력망을 둘로 나누기