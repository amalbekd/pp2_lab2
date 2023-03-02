import re

text = input()

pattern = "a.*b"

x = re.findall(pattern, text)

print(x)