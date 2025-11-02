import sys
import math
pin = sys.stdin.readline


if __name__ == "__main__":
	# N, K = map(int, pin().split())
	# fish_box_list = list(map(int, pin().split()))
	N, K = map(int, "24 5".split())
	# fish_box_list = list(map(int, "5122, 5121, 5125, 5121, 5122, 5121, 5124, 5122, 5118, 5121, 5122, 5120, 5118, 5121, 5120, 5122, 5120, 5121, 5123, 5125, 5119, 5119, 5123, 5126".split(", ")))
	fish_box_list = [329, 9749, 6436, 4945, 7931, 5863, 443, 3013, 8914, 4365, 9414, 9866, 7128, 7213, 5333, 5906, 9324, 3111, 9635, 5504, 7391, 9585, 8267, 2919]
	# N, K = 96, 0
	# fish_box_list = list(range(1, N + 1))

	direction = list(zip([0, -1, 0, 1], [-1, 0, 1, 0]))  # i, j
	n = math.floor((-1 + math.sqrt(1 + 4 * N)) / 2)
	m = N - n * (n + 1)
	r = n < m
	n += r
	m -= n * r
	r = not r
	grid_roll_h, grid_roll_w = n + r, n
	grid_roll = [[-1] * grid_roll_w for _ in range(grid_roll_h)]
	grid_roll_move = [[0] * grid_roll_w for _ in range(grid_roll_h)]
	list_roll_move = [0] * m
	grid_fold_move = [[0] * (N // 4) for _ in range(4)]

	def fish_move(grid1, grid2):
		h, w = len(grid1), len(grid1[0])
		for i in range(h):
			for j in range(w):
				grid2[i][j] = 0
		for i in range(h):
			for j in range(w - 1):
				a = grid1[i][j]
				b = grid1[i][j + 1]
				ab = (abs(a - b) // 5) * (1 if a < b else -1)
				grid2[i][j] += ab
				grid2[i][j + 1] -= ab
		for i in range(h - 1):
			for j in range(w):
				a = grid1[i][j]
				c = grid1[i + 1][j]
				ac = (abs(a - c) // 5) * (1 if a < c else -1)
				grid2[i][j] += ac
				grid2[i + 1][j] -= ac


	k = max(fish_box_list) - min(fish_box_list)
	result = 0
	while K < k:
		result += 1

		### 물고기 추가
		fish_min = min(fish_box_list)
		for i in range(N):
			if fish_box_list[i] == fish_min:
				fish_box_list[i] += 1

		### 골뱅이 처리
		i, j = grid_roll_h - 1, grid_roll_w - 1
		_n, _r, _c, _d = n, r, n, 0
		grid_roll_area = grid_roll_h * grid_roll_w
		box_i = grid_roll_area - 1
		while 0 < _n:
			# print(fish_box_list[box_i], (i, j))
			grid_roll[i][j] = fish_box_list[box_i]
			_c -= 1
			if _c <= 0:
				_n -= _r <= 0
				_r = not _r
				_c = _n
				_d = (_d + 1) % 4
			di, dj = direction[_d]
			i += di
			j += dj
			box_i -= 1
		fish_move(grid_roll, grid_roll_move)
		for i in range(m):
			list_roll_move[i] = 0
		for i in range(m - 1):
			a = fish_box_list[grid_roll_area + i]
			b = fish_box_list[grid_roll_area + i + 1]
			ab = (abs(a - b) // 5) * (1 if a < b else -1)
			list_roll_move[i] += ab
			list_roll_move[i + 1] -= ab
		if 0 < m:
			a = fish_box_list[grid_roll_area - 1]
			b = fish_box_list[grid_roll_area]
			ab = (abs(a - b) // 5) * (1 if a < b else -1)
			grid_roll_move[grid_roll_h - 1][grid_roll_w - 1] += ab
			list_roll_move[0] -= ab
		print(*grid_roll, sep='\n')
		for i in range(grid_roll_h):
			for j in range(grid_roll_w):
				grid_roll[i][j] += grid_roll_move[i][j]
		for i in range(m):
			fish_box_list[grid_roll_area + i] += list_roll_move[i]
		for j in range(grid_roll_w):
			for i in range(grid_roll_h):
				fish_box_list[grid_roll_h * j + i] = grid_roll[grid_roll_h - i - 1][j]
		print(*grid_roll, sep='\n')
		print(fish_box_list)

		### 접기
		grid_fold = [
			fish_box_list[N // 2:N - N // 4][::-1],
			fish_box_list[N // 4:N // 2],
			fish_box_list[:N // 4][::-1],
			fish_box_list[N - N // 4:],
		]
		fish_move(grid_fold, grid_fold_move)
		for i in range(4):
			for j in range(N // 4):
				grid_fold[i][j] += grid_fold_move[i][j]
		for j in range(N // 4):
			for i in range(4):
				fish_box_list[4 * j + i] = grid_fold[3 - i][j]

		k = max(fish_box_list) - min(fish_box_list)
		print(fish_box_list)

	print(result)
