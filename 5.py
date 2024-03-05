m = []
res = 0
for i in range(30):
    s = list(map(int,input().split()))
    m.append(s)

t = m[0][0]
for i in range(1,20):
    t += m[0][i]
    m[0][i] = t

for i in range(1,30):
    k=0
    for j in range(20):
        k+=m[i][j]
        m[i][j] = k + m[i-1][j]

#find max value
for i in range(0,25):
    for j in range(0,15):
        a = m[i+5][j+5] - m[i+5][j] - m[i][j+5] + m[i][j]
        res = max(res,a)

print(res)