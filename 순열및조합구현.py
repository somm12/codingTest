def combination(arr, n):
    
    temp = []
    def combi(comb, start):
        if len(comb) == n:  # 종료 조건 1 : M개를 모두 선택했을 때
            temp.append(comb)
            return
        for i in range(start,len(arr)):
            combi(comb+[arr[i]],i+1)
    combi([],0)
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

# 중복 조합 - 조합에서 해당 인덱스 **이상** 으로 추가.
def combination2(arr,n):
    res = []
    def comb(p, idx):
        if len(p) == n:
            res.append(p)
            return
        for i in range(idx,len(arr)):
            comb(p+[arr[i]],i)
    comb([],0)
    return res

print(combination2([1,2,3,4],2))

# 중복순열 - 순열에서 visited 빼기.
def permutation2(arr,n):
    tmp = []
    # visited = [0]*len(arr)
    def permute(p):
        if len(p) == n:
            tmp.append(p)
            return
        for i in range(len(arr)):
            permute(p+[arr[i]])
    permute([])
    return tmp
print("중복 순열")
print(permutation2([1,2,3],3))