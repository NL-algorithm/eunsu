import sys
pin = sys.stdin.readline

N, M = map(int, pin().split())
r, c, d = map(int, pin().split())
grid = [
	list(map(int, pin().split()))
	for _ in range(N)
]

count = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
while True:
	if grid[r][c] == 0:
		grid[r][c] = 2
		count += 1
	if (
		grid[r + 1][c] == 0 or
		grid[r - 1][c] == 0 or
		grid[r][c + 1] == 0 or
		grid[r][c - 1] == 0
	):  # 청소되지 않은 빈칸이 있다면
		d = (d + 3) % 4
		rr = r + dy[d]
		cc = c + dx[d]
		if grid[rr][cc] == 0:
			r, c = rr, cc
	else:  # 청소할 곳이 없다면
		dd = (d + 2) % 4
		rr = r + dy[dd]
		cc = c + dx[dd]
		if grid[rr][cc] == 1:
			break
		else:
			r, c = rr, cc

print(count)




