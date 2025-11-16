import sys
from collections import deque
pin = sys.stdin.readline

n, m = map(int, pin().split())
padding_grid = [[0] * (m + 2)]
for i in range(n):
	padding_grid.append([0]+list(map(int, pin().split()))+[0])
padding_grid += [[0] * (m + 2)]
target = [
	[0] * (m + 2),
	*[
		[0] + [-1] * m + [0] for _ in range(n)
	],
	[0] * (m + 2),
]

start_i, start_j = 0, 0
for i in range(1, n + 1):
	for j in range(1, m + 1):
		v = padding_grid[i][j]
		if v == 2:
			start_i, start_j = i, j
		elif v == 0:
			target[i][j] = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

q = deque()
q.append((start_i, start_j, 0))
target[start_i][start_j] = 0
while q:
	i, j, k = q.popleft()
	for di, dj in zip(dy, dx):
		new_i, new_j = i + di, j + dj
		v = padding_grid[new_i][new_j]
		if v != 1:
			continue
		if target[new_i][new_j] == -1:
			target[new_i][new_j] = k + 1
			q.append((new_i, new_j, k+1))

for i in range(1, n + 1):
	for j in range(1, m + 1):
		print(target[i][j], end=" ")
	print()
