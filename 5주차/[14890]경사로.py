import sys
pin = sys.stdin.readline

N, L = map(int, pin().split())
grid = [
	list(map(int, pin().split()))
	for _ in range(N)
]

def check(line, length):
	same_h_count = 0
	last_h = line[0]
	for h in line:
		if last_h == h:
			same_h_count += 1
			continue
		if 1 < abs(last_h - h):
			return False  # 높이 초과
		if last_h < h:
			if same_h_count < length:
				return False  # 길이 부족
			same_h_count = 1
			last_h = h
		else:
			if same_h_count < 0:
				return False  # 길이 부족
			same_h_count = 1 - length
			last_h = h
	if same_h_count < 0:
		return False
	return True


# 가로 확인
count = 0
for row in grid:
	if check(row, L):
		count += 1


# 세로 확인
for col in map(list, zip(*grid)):
	if check(col, L):
		count += 1

print(count)
