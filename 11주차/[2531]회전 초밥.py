import sys
pin = sys.stdin.readline

N, d, k, c = map(int, pin().split())
sushi = [
	int(pin()) for _ in range(N)
]

sushi = sushi + sushi

result = 0
for i in range(N):
	s = set(sushi[i:i+k])
	s.add(c)
	result = max(result, len(s))
print(result)
