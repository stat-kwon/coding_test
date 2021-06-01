from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        progresses = deque([x + y for x, y in zip(progresses, speeds)])
        if progresses[0] >= 100:
            complete = 0
            for i in progresses:
                if i >= 100:
                    complete += 1
                else:
                    break
            answer.append(complete)

            for i in range(complete):
                progresses.popleft()
                speeds.popleft()

    return answer

if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))