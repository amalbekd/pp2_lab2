def histogram(t):
    for i in t:
        print('*' * i)


n = input().split()

t = list(map(int, n))

histogram(t)