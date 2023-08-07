def solution(n, l, r):
    answer = 0

    for l in range(l-1, r):
        if check(l):
            answer += 1

    return answer

def check(i):
    if i % 5 == 2:
        return False
    if i < 5:
        return True

    return check(i // 5)
# 프로그래머스 lv2
# n번째 유사 칸토어 비트열에서 l~r 구간에서 1의 개수 찾기.