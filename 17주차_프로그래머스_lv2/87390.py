def solution(n, left, right):
    arr = []
    
    for i in range(left,right+1):
        a = i//n
        b = i%n
        if a > b:
            arr.append(a+1)
        else:
            arr.append(b+1)
    
    return arr
# n^2 배열 자르기
# 입력 개수가 많고, 이진 탐색이 아닌경우, 규칙을 찾는 문제라고 생각하자.
# 주어진 조건 그대로 차근차근 써보면 규칙이 보인다.