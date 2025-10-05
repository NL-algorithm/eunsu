import sys
import math
pin = sys.stdin.readline

N = int(pin())
A_list = list(map(int, pin().split()))
B, C = map(int, pin().split())

result = 0
for a in A_list:
	result += 1
	a -= B
	result += int(max(0, math.ceil(a / C)))
print(result)
