import sys
pin = sys.stdin.readline

dp = [-1] * 10001

N = int(pin())
q = [int(pin()) for _ in range(N)]

def find(n):
	if 0 <= dp[n]:
		return dp[n]
	s = n // 2 + 1
	for i in range(n-3, -1, -3):
		s += i // 2 + 1
	dp[n] = s
	return s

for i in range(N):
	print(find(q[i]))

