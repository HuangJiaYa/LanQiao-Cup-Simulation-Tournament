res = 0
for l in range(0,101):
    for r in range(l,101):
        if r - l >=10:
            res+=1
            
print(res)