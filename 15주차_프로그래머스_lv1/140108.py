def solution(s):
    answer = 0
    while len(s) > 0:
        x = s[0]
        cnt_x = 1
        cnt_other = 0
        for i in range(1,len(s)):
            if s[i] != x:
                cnt_other += 1
            elif s[i] == x:
                cnt_x += 1
            if cnt_other == cnt_x:
                s = s[i+1:]
                answer += 1
                break
        else:
            answer += 1
            break
    return answer
# 문자열 나누기.

# 아래는 더 빠른 코드 -> 왼쪽 부터 오른쪽 방향으로 문자열 확인 하면 되므로, while문이 필요하진 않음.

def solution(s):
    answer = 0
    cnt1 = 0
    cnt2 = 0
    curChar = ""
    for ss in s:
        if cnt1 == 0:
            curChar = ss
        if ss == curChar:
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            answer += 1
            cnt1 = 0
            cnt2 = 0
    if cnt1 > 0:
        answer += 1
    return answer