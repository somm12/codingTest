def solution(lottos, win_nums):
    answer = []
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt = 0
    num_zero = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        if i == 0:
            num_zero += 1
    total = cnt + num_zero
    answer.append(rank[total])
    answer.append(rank[cnt])
    return answer
# 로또의 최고 순위와 최저 순위