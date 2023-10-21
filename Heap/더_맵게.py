import heapq


# 섞은 음식을 스코필 지수를 만드는 함수
def makeScoville(firstS, secondS):
    return firstS + (secondS * 2)


def solution(scoville, K):
    answer = 0

    # scoville heapq으로 변경
    heapq.heapify(scoville)

    # K이상으로 만들기
    while scoville[0] < K:
        # 스코빌 지수를 만들 수 없는 경우
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        answer += 1
        mix = makeScoville(heapq.heappop(scoville), heapq.heappop(scoville))
        heapq.heappush(scoville, mix)
    return answer
