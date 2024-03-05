from math import *
m = int(input())
n = list(map(int,input().split()))
res_min = inf
res_max = 0
for i in range(1,m-1):
    if n[i]<n[i-1] and n[i]<n[i+1]:
        res_max = max(res_max,n[i])
    if n[i]>n[i-1] and n[i]>n[i+1]:
        res_min = min(res_min,n[i])

print(res_max,res_min)