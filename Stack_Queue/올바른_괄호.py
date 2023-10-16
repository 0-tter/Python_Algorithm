def solution(s):
    count = 0

    for bracket in s:
        if bracket == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0