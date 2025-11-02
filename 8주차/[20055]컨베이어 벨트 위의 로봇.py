import sys
pin = sys.stdin.readline


N, K = map(int, pin().split())
A_list = list(map(int, pin().split()))
B_list = [False] * N

result = 0
while True:
	result += 1

	# 1. 컨베이어 벨트 이동
	B_list = [False] + B_list[:-1]
	A_list = A_list[-1:] + A_list[:-1]
	if B_list[-1]:
		B_list[-1] = False

	# 2. 로봇 이동
	for i in range(N-1, -1, -1):
		if B_list[i]:
			if 0 < A_list[i + 1] and B_list[i + 1] == False:
				B_list[i] = False
				B_list[i + 1] = True
				A_list[i + 1] -= 1
	if B_list[-1]:
		B_list[-1] = False

	# 3. 올라기
	if 0 < A_list[0]:
		B_list[0] = True
		A_list[0] -= 1

	# 4. 확인
	if K <= (answer := sum(1 for a in A_list if a == 0)):
		print(result)
		break
