def solution(s):
    answer = ''.join(sorted(s,reverse=True))
    return answer
# 문자열 내림차순으로 배치하기.
# sorted는 sort와 달리 배열을 반환한다.
# sort는 리스트를 대상으로 정렬.