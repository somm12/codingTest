def solution(s):
    answer = ''
    words = s.split(" ")
    
    for w in words:
        if w != ' ':
            for i in range(len(w)):
                if i % 2 == 0:
                    answer += w[i].upper()
                else:
                    answer += w[i].lower()
            answer += ' '
        else:
            answer += w
    answer = answer[:-1]
    
    return answer
# 이상한 문자 만들기