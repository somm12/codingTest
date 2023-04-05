def combination(arr, n):
    
    temp = []
    def combi(comb, start):
        if len(comb) == n:  # 종료 조건 1 : M개를 모두 선택했을 때
            temp.append(comb)
            return
        for i in range(start,len(arr)):
            if i > start:
                combi(comb+[arr[i]],i)
    combi([],-1)
    return temp
   
print(combination([1,2,3,4], 3))

def permutation(arr, r):
    
    # 순열을 저장할 배열
    result = []
    visited = [0]*len(arr)
    # 실제 순열을 구하는 함수
    def permute(p):
        if len(p) == r:
            result.append(p)
            return

        for idx, data in enumerate(arr):
            if not visited[idx]:
                visited[idx] = 1
                permute(p + [data])
                visited[idx] = 0
				# list는 mutable이기 때문에 새로운 리스트를 넘겨준다.

				
    permute([])
    
    return result
print(permutation([1,2,3,4], 2))