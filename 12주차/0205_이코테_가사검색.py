def check(word,q):
    if len(word) != len(q):
        return False
    a = q.split("?")
    for i in range(len(a)):
        if a[i] != '':
            for j in range(len(a[i])):
                if a[i][j] != word[i+j]:
                    return False
    return True

def solution(words, queries):
    global res
    result = []
    for query in queries:
        res = 0
        s = 0
        e = len(words)
        cnt = 0
        while s<=e:
            mid = (s+e)//2
            if cnt == 0:
                for w in words:
                    if check(w,query):
                        cnt += 1
            if cnt >= mid:
                s = mid + 1
                res = mid
            else:
                e = mid - 1
        result.append(res)
    return result
print(solution(["frodo","front","frost","frozen","frame","kakao"],["fro??","????o","fr???","fro???","pro?"]))