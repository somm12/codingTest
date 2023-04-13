def solution(n,left,right):
    answer= [max(i//n,i%n)+1 for i in range(left,right+1)]
    return answer