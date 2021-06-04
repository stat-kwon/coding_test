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
    priorities2 = [1,2,3,4,5,6,7,8, 1, 9, 1, 1, 1]
    location = 0
    location2 = 4
    print(solution(priorities, location))
    print(solution(priorities2, location2))

# any 어쩌고 표현 공부하기


# lambda / filter / map / list compre / zip / enumerate / any

class a:
    # def __repr__(self):
    #     return 'aaaa'
    def a3(self):
        pass
    pass

a1 = a()
a2 = a()
print(a)
print()
print()
print()

a = "1"
b = "2"
print(id(a1))
print(id(a2))
print(id(a1.__class__))
print(id(a2.__class__))
print(dir(a1))

