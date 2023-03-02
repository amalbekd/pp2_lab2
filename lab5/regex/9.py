import re

def f(n):
    return " " + n.group("g1") + ' '

text = input()

pattern = "(?P<g1>[A-Z][a-z]*)"

x = re.sub(pattern, f, text)

print(x)