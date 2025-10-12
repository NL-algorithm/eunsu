import sys
from itertools import product
pin = sys.stdin.readline

N, M = map(int, pin().split())
grid = [
	[6] * (M + 2),
	*[
		[6, *map(int, pin().split()), 6] for _ in range(N)
	],
	[6] * (M + 2),
]

cctv_list = []
wall_count = -((M + 2) * 2 + N * 2)
for i, row in enumerate(grid):
	for j, c in enumerate(row):
		if 1 <= c <= 5:
			cctv_list.append((c, i, j))
		elif c == 6:
			wall_count += 1
cctv_count = len(cctv_list)
cctv_rot = [
	[],
	[[0], [1], [2], [3]],
	[[1, 3], [0, 2]],
	[[0, 1], [1, 2], [2, 3], [3, 0]],
	[[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
	[[0, 1, 2, 3]],
]
cctv_rot_len = [len(r) for r in cctv_rot]
p = [
	range(cctv_rot_len[c])
	for c, i, j in cctv_list
]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def get_view(grid, i, j, direction):
	count = 0
	while True:
		if grid[i][j] == 6:
			break
		if grid[i][j] != 9:
			grid[i][j] = 9
			count += 1
		i += dy[direction]
		j += dx[direction]
	return count

best_min = N * M + 1
for cctv_r in product(*p):
	grid_copy = [
		row[:] for row in grid
	]
	count = N * M - wall_count
	for cctv_num, r_num in enumerate(cctv_r):  # 방향 번호
		cctv_type, i, j = cctv_list[cctv_num]
		# print("cctv_num:", cctv_num, "cctv_type:", cctv_type)
		for direction in cctv_rot[cctv_type][r_num]:  # 실제 방향
			# print(cctv_r, r_num, direction)
			count -= get_view(grid_copy, i, j, direction)
	best_min = min(best_min, count)

print(best_min)
