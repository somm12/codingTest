def solution(keymap, targets):
    answer = []
    dict = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in dict:
                if dict[key[i]] > i+1:
                    dict[key[i]] = i+1
            else:
                dict[key[i]] = i+1
    for t in targets:
        cnt = 0
        for i in range(len(t)):
            if t[i] in dict:
                cnt += dict[t[i]]
            else:
                cnt = -1
                break
        answer.append(cnt)    
           
            
    return answer
# 대충 만든 자판