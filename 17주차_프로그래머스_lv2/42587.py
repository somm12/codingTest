from collections import deque
def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))]
    q = deque(priorities)
    idx = deque(idx)
    while q:
        v = q.popleft()
        i = idx.popleft()
        if q and v < max(q):
            q.append(v)
            idx.append(i)
        else:
            answer += 1
            if i == location:
                return answer
# 프린터 
# 아래 풀이처럼 enumerate를 이용하면 배열의 값과 idx를 동시에 접근가능.
# any를 쓰면 하나라도 true인지 확인.
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

    

