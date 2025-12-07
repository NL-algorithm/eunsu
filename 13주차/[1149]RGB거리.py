import sys
pin = sys.stdin.readline


N = int(pin())
r, g, b = 0, 0, 0

for i in range(N):
	R, G, B = map(int, pin().split())
	r, g, b = min(g, b) + R, min(r, b) + G, min(r, g) + B

print(min(r, g, b))
