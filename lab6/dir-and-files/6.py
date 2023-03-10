import os
import string 

letter = string.ascii_uppercase

for i in letter:
    z = i + '.txt'
    with open(z, 'x') as file:
        file.write(" ")
        file.close()