def gcd(a,b):
    while b !=0 :
        a,b = b, a%b
    return a
def check(arr, x):
    for i in arr:
        if i % x == 0:
            return False
    # x는 arr의 모든 원소로 나눌 수 없음
    return True
def solution(arrayA, arrayB):
    answer = 0
    first = arrayA[0]
    for i in arrayA:
        first = gcd(first,i)
    
    if check(arrayB, first):
        answer = max(answer,first)
    
    second = arrayB[0]
    for i in arrayB:
        second =gcd(second,i)
    
    if check(arrayA, second):
        answer = max(answer,second)
        
    
    
    return answer