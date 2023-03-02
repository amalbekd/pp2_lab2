import re

text = input()

pattern = "^ab*$"

x = re.findall(pattern, text)

print(x)