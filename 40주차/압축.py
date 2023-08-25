def solution(msg):
    answer = []
    dict = {}
    for i in range(65, 91):
        dict[chr(i)] = i-64
    number = 27
    
    while len(msg) >0:
        long = []
        # 제일 긴 문자열 w 찾기
        for i in range(len(msg)+1):
            tmp = msg[:i]
            if tmp in dict:
                # 문자열의 길이, 문자열, 해당 문자열을 다음 인덱스 i
                long.append((len(tmp),tmp,i))
         
        long.sort(key =lambda x:-x[0])
        w = long[0][1]
        # 사전에서 인덱스 찾기
        idx = dict[w]
        answer.append(idx)
        # w제거 
        msg = msg[long[0][2]:]
        # 아직 남으면 w+ c(다음 단어) 사전 등록
        if len(msg) > 0:
            dict[w+msg[0]] = number
        number += 1 # 인덱스 번호 증가
        
    return answer
# 프로그래머스 문제