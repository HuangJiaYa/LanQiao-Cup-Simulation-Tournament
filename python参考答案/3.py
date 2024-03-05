import math
res = 0
def isZhiShu(n:int):
    if n==1:
        return False
    m = int(math.sqrt(n))
    for i in range(2,m+1):
        if n % i == 0:
            return False
    return True

def judge(n):
    if isZhiShu(n):
        s = str(n)
        cnt = 0
        for i in s:
            cnt+=int(i)

        if cnt==23:
            return True
        else:
            return False

    else:
        return False

for i in range(1,1000001):
    if judge(i):
        res+=1

print(res)
