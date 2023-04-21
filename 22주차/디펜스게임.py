from heapq import heappush, heappop

def solution(n, k, enemy):
    hq = []
    for round, monster in enumerate(enemy):
        heappush(hq, monster)
        # 무적권 k개를 모두 쓸 때(제일 큰 수 k개에 사용), 
        # 현재까지 남은 제일 작은 수(병사로 소모)는 n에서 뺀다.
        
        # 빼고 나서 n이 0보다 작다면, return 현재의 인덱스 => 최대 라운드 수 의미.
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return round
    # 만약 k >= 적군 수 라면, 끝까지 push만 하고 for문 종료. 적군의 배열 길이 반환.
    return len(enemy)

# 현재 범위까지의 가장 작은 숫자는 병사를 소모하여 적을 막고, 큰 숫자는 무적권을 써야 최대 라운드
# 갈 수 있다는 아이디어 문제를 풀 수 있다.
