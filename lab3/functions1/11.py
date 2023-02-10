def palindrome(s):
    t = s[::-1]

    if t == s:
        print('True')
    else:
        print('False')

s = input()

palindrome(s)