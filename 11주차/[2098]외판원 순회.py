import sys
from collections import defaultdict
pin = sys.stdin.readline

def generate_mask(bit_length, k, exclude_bit):
	main_bit = (1<<bit_length) - 1
	main_bit &= ~(1 << exclude_bit)
	for i in range(bit_length):
		if i == exclude_bit:
			continue
		yield i, main_bit & ~(1 << i)

if __name__=="__main__":
	N = int(pin())
	W = [
		list(map(int, pin().split()))
		for _ in range(N)
	]

	# dp = [defaultdict(lambda: float("inf"), {i: 0}) for i in range(N)]
	# dp = [{i: 0} for i in range(N)]
	dp = [[float("inf")]*(2**N) for i in range(N)]

	for level in range(1, N):  # 방문 수
		for dst in range(1, N):
			target_dp = dp[dst]
			# for temp, mask in generate_mask(level+1, dst):
			for mask in range(2**N):
				if mask.bit_count() != level:
					continue
				cost = W[temp][dst]
				if cost == 0:
					continue
				new_mask = mask | (1 << temp)
				target_dp[new_mask] = min(target_dp[new_mask], dp[i][mask] + cost)
