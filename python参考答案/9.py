n,m = map(int,input().split())
g = []
res = 0
for i in range(n):
    s = input()
    g.append(s)

def fun(i,j):
    t = 1
    while True:
        x1, y1, x2, y2, x3, y3 = i - t, j - t, i - t, j + t, i + t, j
        if x1<0 or y1<0 or x2<0 or y2<0 or x3<0 or y3<0:
            break
        elif x1>=n or y1>=m or x2>=n or y2>=m or x3>=n or y3>=m:
            break
        if g[i][j]==g[x1][y1]==g[x2][y2]==g[x3][y3]:
            t+=1
        else:
            break
    return t-1

for i in range(1,n-1):
    for j in range(1,m-1):
        res = max(res,fun(i,j))

print(res)
# for i in g:
#     print(i)