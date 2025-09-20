import sys
pin = sys.stdin.readline
import heapq

N = int(pin())
card_heapq = [
	int(pin()) for _ in range(N)
]

heapq.heapify(card_heapq)

comp_count = 0
while 1 < len(card_heapq):
	a, b = heapq.heappop(card_heapq), heapq.heappop(card_heapq)
	comp_count += a + b
	heapq.heappush(card_heapq, a + b)

print(comp_count)

