def go(length,s):
    arr = []
    cnt = 0
    for i in range(0,len(s),length):# length 씩 단위를 끊어서 arr에 append
        if (i + length) > len(s):# index out of range 대비
            arr.append(s[i:])
        else:
            arr.append(s[i:i+length])
    prev = arr[0]# 문자열 압축을 위해 이전 문자열과 비교하기 위해서 prev를 저장.
    result = ''# 압축결과를 저장하기 위한 변수.
    for v in arr:
        if v == prev:
            cnt += 1
        else: # 다르면 result에 압축 결과를 저장한 후, prev와 cnt 업데이트. 1은 생략.
            if cnt == 1:
                result += prev
            else:
                result += (str(cnt)+prev)
            prev = v
            cnt = 1
    if cnt == 1:# 마지막에 남은 문자열 압축 부분 더하기.
        result += prev
    else:
        result += (str(cnt)+prev)
    
    return len(result)# 길이 반환.

def solution(s):
    answer  = 1000# 최대 1000 길이 
    for i in range(1, len(s)+1):# 압축할 단위를 만든다.
        answer = min(answer,go(i,s))
    
    return answer
# 이코테 구현 문제 풀기.