
import sys
import math
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    x, y = (int(val) for val in line.split(SEPARATOR))

    print((x+y),(x*y))