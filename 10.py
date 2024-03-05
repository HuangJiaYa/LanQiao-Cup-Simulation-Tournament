m=int(input())
step=list(map(int,input().split()))
dp=[0]*(m+1)
dp[0]=1
for i in range(1,m+1):
    for j in step:
        if i-j>=0:
            dp[i]=dp[i]+dp[i-j]
print(dp[-1]%1000000007)
#print(dp)