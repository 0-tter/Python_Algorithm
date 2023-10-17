def solution(price, money, count):
    answer = -1
    i = 0
    sum2 = 0
    for i in range(count+1):
        sum2 += price * i
        answer = sum2 - money
        if answer <= 0:
            answer = 0
    return answer