def solution(arr):
    answer = [0,0]
    def comp(lx,ly,n):
        tmp = arr[lx][ly]
        for i in range(lx,lx+n):
            for j in range(ly,ly+n):
                if tmp != arr[i][j]:
                    comp(lx,ly,n//2)
                    comp(lx,ly+n//2,n//2)
                    comp(lx + n//2,ly,n//2)
                    comp(lx + n//2,ly + n//2,n//2)
                    return
        answer[tmp] += 1 
    comp(0,0,len(arr))
    return answer
