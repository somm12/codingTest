def solution(record):
    answer = []
    dict = {}
    for i in record:
        c = i.split()
        if c[0] == 'Enter':
            dict[c[1]] = c[2]
        elif c[0] == 'Change':
            dict[c[1]] = c[2]
    for i in record:
        c = i.split()
        if c[0] == 'Enter':
            s = dict[c[1]] + '님이 들어왔습니다.'
            answer.append(s)
        elif c[0] == 'Leave':
            s = dict[c[1]] + '님이 나갔습니다.'
            answer.append(s)
    return answer
            
# 오픈 채팅방