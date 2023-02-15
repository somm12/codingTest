from bisect import bisect, bisect_left, bisect_right


def find(arr, left,right):
    idx1 = bisect_left(arr,left)
    idx2 = bisect_right(arr,right)
    return idx2-idx1
def solution(words, queries):
    ans = []
    word = [[] for _ in range(10001)]
    reversed_word = [[] for _ in range(10001)]
    for w in words:
        word[len(w)].append(w)
        reversed_word[len(w)].append(w[::-1])
    for i in range(10001):
        word[i].sort()
        reversed_word[i].sort()
    for q in queries:
        if q[0] == '?':
            q = q[::-1]
            cnt = find(reversed_word[len(q)], q.replace('?','a'),q.replace('?','z'))
        else:
            cnt = find(word[len(q)], q.replace('?','a'),q.replace('?','z'))
        ans.append(cnt)
    return ans
solution(["frodo","front","frost","frozen","frame","kakao"],["fro??","????o","fr???","fro???","pro?"])
