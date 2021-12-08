# 피보나치 수열 (보텀 업 다이나믹 프로그래밍)
d = [0] * 100

# 첫 번째 피보나치 수와 두번 째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 4

# 피보나치 함수를 반복문으로 구현
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])