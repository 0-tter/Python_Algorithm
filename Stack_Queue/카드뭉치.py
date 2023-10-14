def solution(cards1, cards2, goal):
    # goal을 하나씩 검사합니다.
    for i in goal:

        # 만약 cards1이 비어있지 않고, 현재 단어(i)가 cards1의 맨 앞에 있는 경우
        if cards1 and i == cards1[0]:
            del cards1[0]  # cards1에서 맨 앞의 원소를 제거합니다.

        # cards2가 비어있지 않고, 현재 단어(i)가 cards2의 맨 앞에 있는 경우
        elif cards2 and i == cards2[0]:
            del cards2[0]  # cards2에서 맨 앞의 원소를 제거합니다.

        # 현재 단어를 cards1 또는 cards2에서 찾을 수 없으면 "No"를 반환합니다.
        else:
            return "No"

    # 모든 단어를 순서대로 검사하고 "No"가 반환되지 않았다면 "Yes"를 반환합니다.
    return "Yes"