def solution(k, score):
    result = []  # 매일 발표된 명예의 전당의 최하위 점수를 저장할 리스트
    k_scores = []  # 현재 날짜까지의 k번째 점수 목록

    for i in score:

        k_scores.append(i)  # 현재 날짜의 점수를 k_scores에 추가
        k_scores.sort(reverse=True)  # 내림차순으로 정렬

        # k_scores 리스트의 길이가 k보다 크면 가장 낮은 점수 제거
        if len(k_scores) > k:
            k_scores.pop()

            # 매일 명예의 전당에 추가되는 최하위 점수를 result에 추가
        result.append(k_scores[-1])

    return result