import sys
from collections import defaultdict

pin = sys.stdin.readline


R, C, K = map(int, pin().split())
grid = [
	[-1] * (C + 2),
	*[
		[-1]+[-1 if c == 'T' else 0 for c in pin().strip()]+[-1] for _ in range(R)
	],
	[-1] * (C + 2),
]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
data = defaultdict(int)

def dfs(i, j, c):
	if grid[i][j] != 0:
		return
	if i == 1 and j == C:
		data[c + 1] += 1
		return
	grid[i][j] = c + 1
	for di, dj in zip(dx, dy):
		dfs(i+di, j+dj, c + 1)
	grid[i][j] = 0

dfs(R, 1, 0)

print(data[K])


