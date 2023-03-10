import os
os.chdir('C:/pp2')
print(os.getcwd())

x = input()

if os.path.exists(x):
    print(True)
else:
    print(False)