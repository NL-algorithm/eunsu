import sys
pin = sys.stdin.readline


N = int(pin())

grid = [
	list(map(int, pin().split())) for _ in range(N)
]


def move_left(board):
	board = [row[:] for row in board]
	for i, row in enumerate(board):
		new_row = [c for c in row if c != 0]
		j = 0
		while j < len(new_row) - 1:
			if new_row[j] == new_row[j + 1]:
				new_row[j] *= 2
				del new_row[j + 1]
			j += 1
		new_row += [0] * (N - len(new_row))
		board[i] = new_row
	return board


def move4(board, d=0):

	if 5 <= d:
		max_tile = 0
		for row in board:
			max_tile = max(max_tile, max(row))
		return max_tile

	d += 1
	a = move4(move_left(board), d)
	ro = list(map(list, zip(*board)))[::-1]
	b = move4(move_left(ro), d)
	ro = list(map(list, zip(*ro)))[::-1]
	c = move4(move_left(ro), d)
	ro = list(map(list, zip(*ro)))[::-1]
	d = move4(move_left(ro), d)

	return max(a, b, c, d)


print(move4(grid))

