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
# 간선이 노드가 작은 순서로 입력되지 않을 경우, parent 배열을 참조했을 때, 트리가 2개로 나누어 지지않을 수 있다.
#예) [[1, 4], [2, 5], [5, 1], [6, 3]] => 5의 부모는 2였으나, union할 때, parent[2] = 1이 되므로
# 여전히 5의 부모는 2가 되어버림.
# parent) [0, 1, 1, 3, 1, 2, 3]
# 따라서 find로 제대로 부모를 찾는 방법으로 트리를 두 개로 나누어 볼 수 있다.