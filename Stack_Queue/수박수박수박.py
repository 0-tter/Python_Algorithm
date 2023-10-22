def solution(n):
    answer = ''
    su = '수', '박'
    j = 0
    for i in range(n):
        answer += su[j]
        j += 1
        if j == 2:
            j = 0

    return answer