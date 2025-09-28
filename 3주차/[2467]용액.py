import sys
pin = sys.stdin.readline

N = int(pin())
solution_list = list(map(int, pin().split()))

l, r = 0, N - 1
find_l, find_r = 0, N - 1
abs_min = float('inf')
while l < r:
	l_v, r_v = solution_list[l], solution_list[r]
	if (v := abs(r_v + l_v)) < abs_min:
		abs_min = v
		find_l, find_r = l_v, r_v
	if 0 < r_v + l_v:
		r -= 1
	else:
		l += 1
print(find_l, find_r)
