def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)  # i가 1이면 0, 1이 아니면 1을 대입
        for j in range(2, int(i**0.5)+1): 
            if i%j == 0:
                if i//j <= 10000000:
                    k = i//j  # j가 2부터 커지기 때문에 처음 만나는 i//j 결과 값인 그 몫이 약수 중 가장 큰 값
                    break
                else: # i//j가 1000만 보다 커진다면, j가 해당 답이 될 수 있음. => 1000만 범위 제약 때문.
                    k = j
        answer.append(k)
    
    return answer