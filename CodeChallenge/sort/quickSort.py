# 퀵 정렬의 시간복잡도 O(NlogN)
# 이미 정렬된 경우(최악의 경우) O(N제곱)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    print([left_side] + [pivot] + [right_side])
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


