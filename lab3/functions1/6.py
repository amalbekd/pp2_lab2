def reverse(s):
    t = s.split()[::-1]
    for i in t:
        print(i, end = ' ')

s = input()

reverse(s)