'''
<문제>
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.

만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.

입출력 예
name	return
"JEROEN"	56
"JAN"	23
'''

# ord 연습
print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print('A-Z 갯수 :', ord('Z') - ord('A') + 1)
print(ord('Z') - ord('A'))
print(ord('A') - ord('A'))
print()

# 첫 시작이 'AAA'라고 가정
answer = 0
name = 'JAZ'
check = [0]*len(name)


def lef_right(idx,i):
    if i == name[0]:
        pass
    elif i == name[-1]:
        pass
    else:
        if ord(name[idx-1]) > ord(name[idx+1]):
            pass
        else:
            pass

for idx, i in enumerate(name):

    if idx == 0:
        if ord(i) == ord('A'):
            pass
        elif ord(i) - ord('A') < 13:
            answer += ord(i) - ord('A') #
        else:
            answer += ord('Z') - ord(i)
    else:
        if ord(i) - 65 < 13:
            pass
        else:
            pass
##############################################################################################


# 못푼 이유 : 한번에 다하려고 하다보니 복잡해짐
# 상하좌우 한번에 생각할 필요가 없을듯
# 먼저 위아래 부터 처리해보기
updown = [[ord(i) - ord('A'), ord('Z') - ord(i) + 1] for i in name]
print(updown)
updown = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
print(updown)

answer += sum(updown)
print(answer)
print()

# 이제 좌우만 생각해주면 됨
# 좌우를 짜는 것부터 구글링을 통해서 비슷한 코드를 찾아봄


name = 'JAAZ'
name2 = "JEROEN"
name3 = "JAN"


# 블로그에서 가져온 다른 사람 풀이
def solution(name):
    cnt = 0  # 총 이동 횟수
    a_cnt = 0  # 'A'의 개수
    a_max = 0  # 'A'의 최대개수
    idx = 0  # 최대'A'개수 문자열의 마지막 인덱스
    a_startIdx = 0  # 최대'A'개수 문자열의 첫번째 인덱스
    wander_cnt = 0  # 좌우로 왔다갔다하는 횟수 카운트

    # 위, 아래 조이스틱 계산
    for i, n in enumerate(name):
        if n == 'A':  # 'A'개수의 최대값과 그 인덱스 계산
            a_cnt += 1
            if a_cnt > a_max:
                a_max = a_cnt
                idx = i
        else:
            cnt += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
            a_cnt = 0
    print(cnt, a_cnt, a_max)

    # 최대'A'개수의 시작 인덱스
    a_startIdx = idx - a_max + 1

    # 최대'A'가 맨 앞이나 맨 끝에 있는 경우
    if a_startIdx == 0 or idx == len(name) - 1:
        cnt += len(name) - 1 - a_max  # a_max개만큼 이동 안해도 됨
    else:
        left = len(name) - idx - 1  # 최대'A'뒤에 남아있는 문자의 개수
        if a_startIdx <= left:  # 뒤에 문자가 앞에 문자개수보다 많은 경우
            wander_cnt = (a_startIdx - 1) * 2 + left
        else:
            wander_cnt = (a_startIdx - 1) + left * 2
        cnt += min(wander_cnt, len(name) - 1)  # 그냥 한쪽방향으로 모두 이동하는 것과 비교

    return cnt

print(solution(name))
