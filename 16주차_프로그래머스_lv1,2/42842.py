def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            b = (yellow)//i
            if (i + b) == (brown-4)//2:
                if i >= b:
                    return [i+2,b+2]
                else:
                    return [b+2,i+2]
                
    
    return answer
# 카펫