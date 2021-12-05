# 선택 정렬의 시간복잡도 O(N제곱)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i
    # 한바퀴 돌며 가장 작은 인덱스 찾기
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            print(array)
    # 스와프
    array[i], array[min_index] = array[min_index], array[i]