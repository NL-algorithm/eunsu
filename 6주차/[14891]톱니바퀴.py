import sys
pin = sys.stdin.readline

gear_list = [
	list(map(int, pin().strip()))
	for _ in range(4)
]
K = int(pin())
query = [
	map(int, pin().split())
	for _ in range(K)
]

def spin(gear, w):
	return gear[-w:] + gear[:-w]

def check_chain(i):
	chain = [i]
	for j in range(i, 0, -1):  # 왼쪽
		if gear_list[j-1][2] != gear_list[j][6]:
			chain.append(j-1)
		else:
			break
	for j in range(i, 3):  # 오른쪽
		if gear_list[j][2] != gear_list[j+1][6]:
			chain.append(j+1)
		else:
			break
	return chain

def show():
	for i in range(4):
		print(gear_list[i][7], gear_list[i][0], gear_list[i][1], end="  ")
	print()
	for i in range(4):
		print(gear_list[i][6], ".", gear_list[i][2], end="  ")
	print()
	for i in range(4):
		print(gear_list[i][5], gear_list[i][4], gear_list[i][3], end="  ")
	print()

for target_gear, w in query:
	target_gear -= 1
	chain = check_chain(target_gear)
	for c in chain:
		gear_list[c] = spin(gear_list[c], w * ((-1) ** abs(target_gear-c)))

print(
	sum(gear[0] * (2**i) for i, gear in enumerate(gear_list))
)
