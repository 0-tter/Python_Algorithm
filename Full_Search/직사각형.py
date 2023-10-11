def solution(sizes):
    max_width = max_height = 0

    for size in sizes:
        # 각 원소의 최댓값과 최솟값을 구합니다.
        max_width = max(max_width, max(size))
        max_height = max(max_height, min(size))

    answer = max_width * max_height
    return answer