import sys
pin = sys.stdin.readline

def find(grid: list, i):
	i_1 = i + 1
	if N == i_1:
		return sum(grid[0])
	count = 0
	row_max = N - i
	grid_0 = grid[0]
	for j in range(N):
		if not grid_0[j]:
			continue
		new_grid = [v[:] for v in grid[1:]]
		for r in range(1, row_max):
			gr = new_grid[r - 1]
			gr[j] = False
			if 0 <= (a := j - r):
				gr[a] = False
			if (b := j + r) < N:
				gr[b] = False
		count += find(new_grid, i_1)
	return count

N = int(pin())
grid = [[True]*N for _ in range(N)]

print(find(grid, 0))
import time
start_time = time.time()
print(find(grid, 0))
print(time.time() - start_time)
