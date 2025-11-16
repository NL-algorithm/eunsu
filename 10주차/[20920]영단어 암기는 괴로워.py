import sys
from collections import defaultdict
pin = sys.stdin.readline

N, M = map(int, pin().split())
word_memo = defaultdict(int)
for i in range(N):
	text = pin().strip()
	if len(text) < M:
		continue
	word_memo[text] += 1

word_memo = sorted(
	list(word_memo.items()),
	key=lambda x: (-x[1], -len(x[0]), x)
)
print(*[w for w, i in word_memo], sep="\n")
