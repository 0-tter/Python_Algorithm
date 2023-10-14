def solution(s, skip, index):
    alps = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(skip))
    # 알파벳 문자열에서 스킵을 빼고 변수 alps에 저장
    alps_num = len(alps)
    # 변수 alps_num에 alps에 있는 알파벳 개수 저장
    answer = ''

    for char in s:  # 한 문자씩 반복
        answer += alps[(alps.index(char) + index) % alps_num]
        # 1. 현재 문자 char가 alps 리스트에서 몇 번째 위치에 있는지 찾기
        # 2. 주어진 index만큼 더한 후 새로운 위치를 계산하고 유효한 범위 내로 조정
        # 3. 새로운 위치에 해당하는 알파벳을 결과 문자열에 추가
    return answer