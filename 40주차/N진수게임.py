def solution(n,t,m,p):
    answer =''
    
    def convert(num, base):# base(N진법) 으로 변환한 문자열 반환.
        temp = "0123456789ABCDEF" # 16진법 까지 나타내므로 모두 0 ~ F까지 나타낼 수 있다.
        q, r = divmod(num, base) # 파이썬 내장함수로, q는 몫, r는 나머지를 뜻함.

        if q == 0:# 몫이 0 이라면 나머지 반환. (여기서 10 ~ 15는 조건에 따라 A~ F로 나타냄)
            return temp[r]
        else:
            # q를 base로 변환
            # 즉, n진수의 다음 자리를 구함
            return convert(q, base) + temp[r] # 이어서 나머지를 하나씩 구해서 재귀로 합침. 
    
    
    for i in range(t*m):# 변환 시킨 십진수를 answer 에 넣기.
        answer += convert(i,n)
    
    answer = list(answer)
    # (p-1 인덱스 부터 ~ t*m -1 인덱스 까지 m씩 건너뛴 숫자 => 튜브가 말해야하는 숫자.
    return ''.join(answer[p-1:t*m:m]) # join과 인덱싱을 이용해서 정답 반환.
# 프로그래머스 카카오문제.