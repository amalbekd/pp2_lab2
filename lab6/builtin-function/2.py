s = input()

l = sum([1 for i in s if i.islower()])
u = sum([1 for j in s if j.isupper()])


print("lower", l)
print("upper", u)
