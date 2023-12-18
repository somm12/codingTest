n = int(input())
real = [i for i in range(1,n+1)]
arr = list(map(int,input().split()))
maxK = -1
for k in range(1,n+1):# 최대 k 구하기.
    if 2**k < n:
        maxK = max(maxK,k)
    else:
        break

def solution():# 거꾸로 카드 섞기.
    for k1 in range(1,maxK+1):
        for k2 in range(1,maxK+1):
            tmp = arr[:]
            
            for i in range(k2+1,0,-1):# k2 섞기.
                
                if i >= 2:# 2 이상의 단계 => 앞에서 2의 k2-i+1 제곱 만큼 개수를 해당 개수 만큼 뒤로 보내기.
                    cnt = 2**(k2-i + 1)
                    tmp = tmp[cnt:2*cnt] + tmp[:cnt] + tmp[2*cnt:]
                else:# 1단계 => 앞에서 2의 k2제곱 만큼 맨 뒤로 보내기
                    tmp = tmp[2**k2:] + tmp [:2**k2]
                
            for i in range(k1+1,0,-1):
                
                if i >= 2:
                    cnt = 2**(k1-i + 1)
                    tmp = tmp[cnt:2*cnt] + tmp[:cnt] + tmp[2*cnt:]
                else:
                    tmp = tmp[2**k1:] + tmp [:2**k1]
                
            if tmp == real:
                return [k1, k2]

answer = solution()
print(answer[0],answer[1])
# 백준