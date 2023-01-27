from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if count > len(dist):
        answer = - 1
    return answer
# 이처럼 원형으로 나열된 데이터를 처리하는 경우에는 문제 풀이를 간단히 하기 위해 길이를 2배로 늘려서 원형을 
# 일자 형태로 만드는 작업을 해주면 유리함.
# 다시 풀어보기.
