n = int(input())
p = int(input())
cnt = 0
parent = [i for i in range(n+1)]
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b= find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(p):
    g = int(input())
    root = find_parent(parent,g)
    if root == 0:
        break
    cnt += 1
    union(parent,root,root-1)
print(cnt)

# 서로소 집합을 이용하는 문제로, 
# 탑승구를 중심으로 서로 다른 집합으로 나태낼 수 있다.(탑승구 개수에 맞춰서 도킹)
# 가장 큰 번호 탑승구 먼저 도킹
# 0 번 탑승구도 있다고 가정
# 집합의 루트가 0 일 때 더이상 도킹할 수 없다고 판단.

# 내 생각: 이 탑승구의 번호의 루트가 곧 도킹할 수 있는 탑승구 개수와 같다.
# 0 1-2 3 4: 즉 1과 2를 union하면 1번부터 2번까지 도킹할 수 있는 탑승구 중에서 1개만 도킹할 수 있다는 의미.

# 서로소 집합이라면, 어떤 값을 중심으로 문제를 해결할지 선택하자.