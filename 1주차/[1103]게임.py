import sys
pin = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, pin().split())
grid = [
	list(pin().strip())
	for _ in range(N)
]
grid_max = [
	[0] * M
	for _ in range(N)
]

def move(grid, pos, log: set, n):
	if n == -1:
		return -1
	r, c = pos
	if r < 0 or N <= r or c < 0 or M <= c:
		return n
	if pos in log:
		return -1
	v = grid[r][c]
	if v == 'H':
		return n
	v_max = grid_max[r][c]
	if 0 != v_max:
		return v_max + n

	num = int(v)
	value_list = []
	value_list.append(move(grid, (r + num, c), log | {pos}, n + 1))
	value_list.append(move(grid, (r - num, c), log | {pos}, n + 1))
	value_list.append(move(grid, (r, c + num), log | {pos}, n + 1))
	value_list.append(move(grid, (r, c - num), log | {pos}, n + 1))
	if -1 in value_list:
		v_max = -1
	else:
		v_max = max(value_list)
	grid_max[r][c] = v_max - n
	return v_max
print(move(grid, (0, 0), set(), 0))
