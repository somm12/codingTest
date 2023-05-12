def solution(citations):
    citations.sort()
    length = len(citations)
    for i,v in enumerate(citations):
        if v >= length - i:
            return length - i
    return 0
# 프로그래머스 h-index
# n편 중 h번 이상 인용된 논문이 h편이상, 나머지 논문은 h번 이하로 인용됬을 때, h의 최댓값.
#  0   1   3   5   6
# [0] [1] [2] [3] [4] (인덱스)
# 최댓값은 h편이상이기 때문에 len(citations).
# 정렬 이후, 현재 인용된 횟수이상으로 인용된 논문 개수는 length - i(현재 인덱스).(정렬을 했으니, 자동으로 뒤는 해당 값 이상.)
# 하지만 인용 횟수 범위가 0이상이기 때문에 [0,0,0,0] 일 경우 답이 0. -> return 0으로 따로 빼준다.