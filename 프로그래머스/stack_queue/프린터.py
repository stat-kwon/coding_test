from collections import deque

def solution(priorities, location):
    index = [i for i in range(len(priorities))]
    prior_inx = list(zip(priorities, index))
    queue = deque(prior_inx)

    answer = 0
    loc = 0
    while queue:
        a = queue.popleft()
        for i in queue:
            if i[0] > a[0]:
                queue.append(a)
                break
        else:
            answer += 1
            loc = a[1]
            if loc == location:
                break
    return answer

if __name__ == '__main__':
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))

# any 어쩌고 표현 공부하기