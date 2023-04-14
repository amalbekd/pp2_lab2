import re

text = input()

pattern = "^ab{2,3}$"

x = re.search(pattern, text)

print(x)