from sys import stdin
from functools import cache
pin = stdin.readline

if __name__ == "__main__":
	N, K = map(int, pin().split())
	items = [tuple(map(int, pin().split())) for _ in range(N)]

	@cache
	def get_backpack(weight, idx):
		if weight <= 0: return 0
		if idx < 0: return 0
		w, v = items[idx]
		return max(
			get_backpack(weight, idx - 1),
			(get_backpack(weight - w, idx - 1) + v) if weight - w >= 0 else 0,
		)

	print(get_backpack(K, N - 1))