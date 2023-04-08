def solution(seq, k):
    answer = []
    end = 0
    inter = seq[0]
    for start in range(len(seq)):
        while inter < k:
            end += 1
            if end >= len(seq):
                break
            inter += seq[end]
        if inter == k:
            answer.append((end-start+1,start,end))
        inter -= seq[start]
    answer.sort()
    return [answer[0][1],answer[0][2]]
# 연속된 부분 수열의 합
