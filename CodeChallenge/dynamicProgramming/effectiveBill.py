# 효율적인 화폐 구성
# 정수 N, M을 입력 받기
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행
d[0] = 0
for i in range(n): # 화폐의 종류 갯수만큼 반복
    for j in range(array[i], m + 1): # 각 화폐의 단위로 리스트의 길이만큼 반복
        print(j)
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])