
def solution(prices):
    stack = []
    n = len(prices)
    answer = [0]*n
    for i in range(n):
        while stack and stack[-1][1] > prices[i]:# 가격이 떨어지면, 유지되는 기간 갱신.
            
            idx,v = stack.pop()
            answer[idx]= i - idx
        stack.append((i,prices[i]))
    for i,v in stack:# 남은 수들은 끝까지 주식가격이 떨어지지 않는것.
        answer[i] = n-1 - i
        
    return answer

