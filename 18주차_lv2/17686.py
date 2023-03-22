def solution(files):
    answer = []
    arr = []
    for idx in range(len(files)):
        h = ''
        hend = 0
        for i in range(len(files[idx])):
            if not files[idx][i].isdecimal():
                h += files[idx][i]
            else:
                hend=i-1
                break
        num = ''
        for i in range(hend+1,len(files[idx])):
            if files[idx][i].isdecimal() and len(num) < 5:
                num += files[idx][i]
            else:
                break
        arr.append((h,num,idx))
    arr.sort(key=lambda x:(x[0].lower(),int(x[1])))
    for h,num,idx in arr:
        answer.append(files[idx])
    return answer

# 파일명 정렬