import re

text = input()

pattern = "[ ,.]"

x = re.sub(pattern, ":", text)

print(x)