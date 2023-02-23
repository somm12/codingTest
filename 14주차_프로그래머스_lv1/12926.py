def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            a = ord(i) + n
            if 97<= ord(i) <= 122 and a > 122:
                answer += chr(a-122 + 96)
            elif 65 <= ord(i) <= 90 and a > 90:
                answer += chr(a - 90 + 64)
            else:
                answer += chr(a)
        else:
            answer += i
            
    return answer

# 시저 암호