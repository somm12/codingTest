n = int(input())
parent = list(map(int,input().split()))
x = int(input())

parent[x] = -2
delete = [x]# 삭제될 노드 번호.

while delete:
    x = delete.pop() # 삭제될 노드의 자식들을 while문을 통해 제거.
    for i in range(n): 
        if parent[i] == x:# 부모가 x라면 제거 대상, 그리고 해당 노드의 자식도 제거하기 위해 delete에 추가.
            parent[i] = -2
            delete.append(i)

s = set()
total = 0

for v in parent:
    if v != -2:
        total += 1 # 전체 살아남은 노드 개수.
    if v >= 0:
        s.add(v)# 부모인 노드의 개수.

s = list(s)# 부모인 노드들

print(total - len(s))# 남은 리프 노드