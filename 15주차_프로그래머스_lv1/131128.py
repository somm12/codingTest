def solution(X, Y):
    answer = ''
    ans = []
    dict = {}
    for i in X:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in Y:
        if i in dict:
            if dict[i] > 0:
                dict[i] -= 1
                ans.append(int(i))
    if len(ans) == 0:
        return '-1'
    if max(ans) == 0:
        return '0'
    ans.sort(reverse=True)
    return ''.join(str(j) for j in ans)
# 숫자짝꿍