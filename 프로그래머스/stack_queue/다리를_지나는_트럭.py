from collections import deque
def solution(bridge_length, weight, truck_weights):
    ing = deque([0] * bridge_length)
    tk_wei = deque(truck_weights)
    time = 0

    while len(ing):
        time += 1
        ing.popleft()
        if tk_wei:
            if sum(ing) + tk_wei[0] <= weight:
                car = tk_wei.popleft()
                ing.append(car)
            else:
                ing.append(0)
    return time