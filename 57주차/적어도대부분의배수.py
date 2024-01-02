answer = int(1e9)
arr = list(map(int,input().split()))
def gcd(a,b):
    if b == 0:
    	return a
    if a % b == 0:
    	return b
    else:
    	return gcd(b, a % b)
def lcm(a,b):
    return (a*b)//gcd(a,b)

def dfs(start,res):
    global answer
    if len(res) == 3:
        a,b,c = res
        tmp1 = lcm(a,b)
        tmp2 = lcm(tmp1,c)
        
        answer = min(answer,tmp2)
        return
    
    for i in range(start,len(arr)):
        dfs(i+1,res+[arr[i]])
# 최소공배수 == 최대공약수 * (a//최대공약수 * b//최대공약수) == (a*b)//최대공약수
dfs(0,[])
print(answer)
