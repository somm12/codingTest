def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        # 5의 다음 자리값이 5 -9 에 해당하면 10에 도달.
        # 0 -4 면 0으로 도달.
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer
# 마법의 엘리베이터