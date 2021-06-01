'''
문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
입출력 예 설명
입출력 예 #1
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

입출력 예 #2
모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.

따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.
'''

# 생각 정리
# 선입선출 구조를 가져야 한다. -> queue로 구현
# from collections import deque
# queue = deque()
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# print(queue)
#
# queue.popleft()
# print(queue)


# def solution(progresses, speeds):
#     answer = []
#     return answer

# from collections import deque
#
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# ret = [2,1]
# comp = 0

''' 1. queue로 구현하기 위해서 노력함'''
# queue = deque(i for i in progresses)
# print(queue)
#
# print(deque(map((lambda a,b : a+b), queue,speeds)))

# while queue:
#     answer = []
#     work = deque(map((lambda a,b : a+b), queue,speeds))
#     for i in work:
#         if i >= 100:
#             comp += 1
#     if comp != 0:
#         answer.append(comp)
#     comp =0
# print(answer)

# while queue:
#     answer = []
#     work = deque(map((lambda a,b : a+b), queue,speeds))
#     for i in work:
#         if i >= 100:
#             comp += 1
#     if comp != 0:
#         answer.append(comp)
#     comp =0
# print(answer)

''' 2. queue와 while을 사용해서 구현'''
# from collections import deque
#
# answer = []
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# ret = [2,1]
# comp = 0
#
# progresses = deque(progresses)
# print(progresses)
# speeds = deque(speeds)
# print(speeds)
# progresses = deque([x+y for x,y in zip(progresses,speeds)])
# print(progresses)
# print()
# print()
#
# while progresses:
#     progresses = deque([x+y for x,y in zip(progresses,speeds)])
#     if progresses[0] >= 100:
#         print(progresses)
#         progresses.popleft()
#         speeds.popleft()

''' 3. 중간에 100으로 완료된 것 처음거 될때 까지 처리안되도록 구현 '''
# from collections import deque
#
# answer = []
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# ret = [2,1]
#
# progresses = deque(progresses)
# print(progresses)
# speeds = deque(speeds)
# print(speeds)
# progresses = deque([x+y for x,y in zip(progresses,speeds)])
# print(progresses)
# print()
# print()
#
# while progresses:
#     progresses = deque([x+y for x,y in zip(progresses,speeds)])
#     if progresses[0] >= 100:
#         complete = 0
#         for i in progresses:
#             if i >= 100:
#                 complete += 1
#         answer.append(complete)
#         for i in range(complete):
#             progresses.popleft()
#             speeds.popleft()
#         print('answer : {} / progresses : {}'.format(answer,progresses))


''' 4. 연속되게 100 이상인것만 지우는거 구현하면 완성될 듯 '''
# from collections import deque
#
# answer = []
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# ret = [2,1]
#
# progresses = deque(progresses)
# print(progresses)
# speeds = deque(speeds)
# print(speeds)
# progresses = deque([x+y for x,y in zip(progresses,speeds)])
# print(progresses)
# print()
# print()
#
# while progresses:
#     progresses = deque([x+y for x,y in zip(progresses,speeds)])
#     if progresses[0] >= 100:
#         complete = 0
#         for i in progresses:
#             if i >= 100:
#                 complete += 1
#             else:
#                 break
#         answer.append(complete)
#
#         for i in range(complete):
#             progresses.popleft()
#             speeds.popleft()
#
#         print('answer : {} / progresses : {}'.format(answer,progresses))

''' 5. 최종정리 '''
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