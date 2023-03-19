def solution(msg):
    answer = []
    dict = {}
    n = len(msg)
    idx = 27
    ch = [0]*n
    for i in range(65,91):
        dict[chr(i)] = i -64
    for i in range(n):
        now = ''
        if ch[i] == 0:
            for j in range(i,n):
                now += msg[j]
                if now not in dict:
                    answer.append(dict[msg[i:j]])
                    dict[now] = idx
                    idx += 1
                    break
                ch[j] = 1
            else:
                answer.append(dict[now])
    
    
    return answer
# 압축