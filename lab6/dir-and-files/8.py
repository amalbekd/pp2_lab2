import os

dfile = input()
os.chdir(dfile)
x = input()
if os.path.exists(x):
    d = input()
    os.rmdir(d)
else:
    print('not exists')