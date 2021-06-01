from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        value = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if value > i:
                break
        answer.append(cnt)

    return answer