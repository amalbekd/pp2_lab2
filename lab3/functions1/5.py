<<<<<<< HEAD
def permutations(s, t = ''):
 
    if len(s) == 0:
        print(t)
 
    for i in range(len(s)):
 
        T = t + s[i]
        S = s[0:i] + s[i+1:]
 
        permutations(S, T)
 
s = input()
permutations(s)
=======
def permutations(s, t = ''):
 
    if len(s) == 0:
        print(t)
 
    for i in range(len(s)):
 
        T = t + s[i]
        S = s[0:i] + s[i+1:]
 
        permutations(S, T)
 
s = input()
permutations(s)
>>>>>>> 2a979e4717352ef20e11fce5aa6c52f3c54e7091
 