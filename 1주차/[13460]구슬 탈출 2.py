import sys
from collections import deque
from copy import deepcopy
pin = sys.stdin.readline


N, M = map(int, pin().split())
board = []
for i in range(N):
	board.append([])
	for j, t in enumerate(pin().strip()):
		board[i].append(t)

def move_left(board):
	r_goal_flag = False
	b_goal_flag = False
	move_flag = False
	for i in range(len(board)):
		pos = -1
		for j in range(len(board[0])):
			v = board[i][j]
			if v == '#':
				pos = j + 1
			elif v == 'O':
				pos = j
			elif v == 'R':
				if pos != j:
					move_flag = True
					board[i][j] = '.'
					if board[i][pos] == 'O':
						r_goal_flag = True
					else:
						board[i][pos] = 'R'
						pos = pos + 1
				else:
					pos = j + 1
			elif v == 'B':
				if pos != j:
					move_flag = True
					board[i][j] = '.'
					if board[i][pos] == 'O':
						b_goal_flag = True
					else:
						board[i][pos] = 'B'
						pos = pos + 1
				else:
					pos = j + 1
	return board, r_goal_flag, b_goal_flag, move_flag


def step(board, move, n=0):
	move_flag = False
	r_goal_flag, b_goal_flag = False, False
	board = deepcopy(board)
	if move == 0:  # left
		board, r_goal_flag, b_goal_flag, move_flag = move_left(board)
	elif move == 1:  # right
		board = [row[::-1] for row in board]
		board, r_goal_flag, b_goal_flag, move_flag = move_left(board)
		board = [row[::-1] for row in board]
	elif move == 2:  # up
		board_ccw = list(map(list, zip(*board[::-1])))
		board_ccw, r_goal_flag, b_goal_flag, move_flag = move_left(board_ccw)
		board = list(map(list, zip(*board_ccw)))[::-1]
	elif move == 3:  # down
		board_cw = list(map(list, zip(*board)))[::-1]
		board_cw, r_goal_flag, b_goal_flag, move_flag = move_left(board_cw)
		board = list(map(list, zip(*board_cw[::-1])))

	return board, r_goal_flag, b_goal_flag, move_flag


q = deque()
q.extend((board, i, 1) for i in range(4))
goal_n = -1
while q:
	board, move, n = q.popleft()
	board, r_goal_flag, b_goal_flag, move_flag = step(board, move, n)
	if r_goal_flag and not b_goal_flag:
		goal_n = n
		break
	if b_goal_flag:
		continue
	next_n = n + 1
	if 11 <= next_n:
		continue
	if move_flag:
		q.extend((board, i, next_n) for i in range(4))
print(goal_n)
