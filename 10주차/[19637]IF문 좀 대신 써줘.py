import sys
import bisect
pin = sys.stdin.readline

N, M = map(int, pin().split())
memo = []
for i in range(N):
	name, combat_power = pin().split()
	combat_power = int(combat_power)
	memo.append((combat_power, i, name))
memo.sort()

for i in range(M):
	target_combat_power = int(pin())
	j = bisect.bisect_left(memo, (target_combat_power,))
	print(memo[j][2])

