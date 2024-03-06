def solution(a, edges):
    answer = 0
    n = len(a)
    if sum(a) != 0:# 모든 합이 0 이 아니면 가중치를 모두 0으로 만들 수 없음
        return -1
    g = [[] for _ in range(n)]
    for x,y in edges:
        g[x].append(y)
        g[y].append(x)
    parent = [0]* n# 부모를 나타냄.
    parent[0] = -1# 루트인 0의 부모는 -1
    visited =[0]*n
    visited[0] = 1
    stack= [0]
    traversal = [0]# 리프노드 부터 루트 노드 까지의 순서를 담을 배열.
    while stack:
        node = stack.pop()
        for v in g[node]:
            if not visited[v]:
                visited[v] = 1
                stack.append(v)
                traversal.append(v)
                parent[v] = node
   
    for x in traversal[::-1]:# 뒤집으면 리프노드 부터 탐색.
        if a[x] == 0:# 이미 가중치 0이면 넘어가기
            continue
        answer += abs(a[x])# 절댓값이 즉, 행위 개수
        p = parent[x]#  x의 부모 p
        a[p] += a[x]# 자식 가중치를 부모 가중치에 값을 더해줘서 점점 루트로 올리기. ex) 자식이 5, 부모가 3이면, 자식은 -5를 해야하고, 부모는 +5해아함.
        a[x] = 0
    
    return answer