def solution(n, words):
    answer = []
    dict = {}
    prev = ' '
    idx = -1
    
    for i in range(len(words)):
        if words[i] in dict:
            idx = i
            break
        else:
            if len(words[i]) == 1:
                idx = i
                break
            elif prev != ' ' and prev[-1] != words[i][0]:
                idx = i
                break
            else:
                dict[words[i]] = 1
                prev = words[i]
    if idx == -1:
        return [0,0]
    else:
        return [(idx)%n + 1, (idx)//n+1]

# 영어 끝말 잇기