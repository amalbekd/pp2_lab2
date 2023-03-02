def even(n):
    cnt = 0
    while cnt <= n:
        if(cnt % 2 == 0):
            yield cnt
        cnt += 1

n = int(input())
for i in even(n):
  if i < n - 1:
    print(i, end = ' , ')
  else:
    print(i)