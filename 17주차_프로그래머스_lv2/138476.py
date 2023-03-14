def solution(k, tangerine):
    dict = {}
    arr= []
    n = len(tangerine)
    for i in tangerine:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in dict:
        arr.append((i, dict[i]))
    arr.sort(key= lambda x : x[1])
    remain = n - k
    answer = len(arr)
    for i in range(len(arr)):
        if arr[i][1] <= remain:
            remain -= arr[i][1]
            answer -= 1
        else:
            break
    return answer
    
    
# 귤 고르기 -> values() 를 이용하면 간단한 코드로 구현 가능하다.
# 아래는 더 쉬운 코드

def solution(k, tangerine):
    answer = 0
    dict = {}
    for i in tangerine:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for v in sorted(dict.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer