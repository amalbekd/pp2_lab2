s = input()

p = "".join(reversed(s))

print("palindrome") if s == p else print("not palindrome")