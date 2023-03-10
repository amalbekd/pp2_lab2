import os
os.chdir('C:/pp2/labs/lab6/dir-and-files')
with open('test.txt') as line:
    count = 0
    for i in line:
        count += 1
        print(count)