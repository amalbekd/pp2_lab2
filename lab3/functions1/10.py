def unique(thislist):
    k = {}
    g = []
    for i in thislist:
        if(i not in k):
            k[i] = 1
        else:
            k[i] += 1

    
    for x, y in k.items():
        if(y == 1):
            g.append(x)
    return g


n = int(input())
thislist = []
for i in range(n):
    x = int(input())
    thislist.append(x)

print(unique(thislist))
