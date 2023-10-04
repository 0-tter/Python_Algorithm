def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    sorted_reserve = sorted(set_reserve)

    for r in sorted_reserve:
        if r - 1 in set_lost:
            set_lost.remove(r - 1)
        elif r + 1 in set_lost:
            set_lost.remove(r + 1)

    return n - len(set_lost)