from itertools import permutations
def solution(babbling):
    answer = 0
    dict = {'aya': 'A', 'ye': 'B', 'woo': 'C', 'ma':'D'}
    for i in range(len(babbling)):
        for j in dict:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j, dict[j])
    for s in babbling:
        for j in range(len(s)):
            if s[j] not in ('A','B','C','D'):
                break
            if j> 0:
                if s[j] == s[j-1]:
                    break
        else:
            answer += 1
    return answer
# 옹알이2