def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col-1],-x[0]))
    tmp = []
    for i in range(row_begin-1, row_end):
        cnt = 0
        for j in range(len(data[i])):
            cnt += (data[i][j] % (i+1))
        tmp.append(cnt)

    answer = tmp[0]
    for i in range(1,len(tmp)):
        answer = answer ^ tmp[i]
    return answer