import sys
from collections import deque
pin = sys.stdin.readline

line = set()
N, K = map(int, pin().split())

q = deque()
q.append((N, 0))
while q:
	k, count = q.popleft()
	if k == K:
		print(count)
		break
	for a, b in (
		(k+1, count+1),
		(k-1, count+1),
		(k*2, count+1),
	):
		if not (0 <= k <= 100_000):
			continue
		if a not in line:
			q.append((a, b))
			line.add(a)
pass

