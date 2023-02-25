<<<<<<< HEAD
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
=======
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
>>>>>>> 2a979e4717352ef20e11fce5aa6c52f3c54e7091
