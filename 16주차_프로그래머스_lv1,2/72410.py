def removeDuplicates(s):
    chars = []
    prev = None
    for c in s:
        if (prev != c and prev == '.') or prev != '.':
            chars.append(c)
            prev = c
            
    return ''.join(chars)

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalpha() or i.isdigit():
            answer += i
        elif i in ('-','_','.'):
            answer += i
    answer = removeDuplicates(answer)
    
    if answer != '':
        if answer[0] == '.':
            answer = answer[1:]
    if answer != '':
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) == 0:
        answer += 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        t = answer[-1]
        while len(answer) < 3:
            answer += t
    return answer
# 신규아이디 추천