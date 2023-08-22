from collections import deque
def check(a,b):# 두 문자열에서 다른 문자가 1개만 있는지 확인.
    cnt =0 
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False
def solution(begin, target, words):
    
    q = deque()
    q.append((begin, 0))
    visited = [0]*len(words)
    while q: # bfs로 가장 먼저 target에 도달할 때 cnt를 반환.
        now,cnt = q.popleft()
        if now == target:
            return cnt
        for i,v in enumerate(words):
            if not visited[i]:# 이미 방문했던 문자열이라면 이후에도 같은 결과를 내기에 방문처리하기.
                if check(v,now):
                    visited[i] = 1
                    q.append((v,cnt+1))# 변환 한 번 했으므로 +1.
    return 0 # 변환을 할 수 없다면 0 반환.
    
# 프로그래머스 bfs/dfs 단어변환 복습.