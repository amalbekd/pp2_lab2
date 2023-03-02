def f(x):
    cnt = 0
    while(cnt <= x):
        if(cnt % 3 == 0) | (cnt % 4 == 0):
            yield cnt
        cnt += 1

a = int(input())

for i in f(a):
    print(i)