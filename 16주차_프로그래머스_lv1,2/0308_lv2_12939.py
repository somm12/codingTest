def solution(s):
    answer = ''
    l = list(map(int, s.split()))
    answer = ' '.join([str(min(l)),str(max(l))])
    return answer
# lv최댓값과 최솟값