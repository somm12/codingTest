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