def solution(n):
    answer = []
    def hanoi(n,start,to,by):
        if n==1:
            answer.append([start,to])
            return
        hanoi(n-1,start,by,to)
        answer.append([start,to])
        hanoi(n-1,by,to,start)
    hanoi(n,1,3,2)
    return answer
# 하노이 탑