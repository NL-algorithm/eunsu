import sys
pin = sys.stdin.readline


N = int(pin())
flower_list = list(map(int, pin().split()))

memo_dict = {}

for i, v in enumerate(flower_list):
	max_v = 0
	for j, s in memo_dict.items():
		max_v = max(max_v, s + abs(j - v) ** 2)
	memo_dict[v] = max_v

print(max(memo_dict.values()))