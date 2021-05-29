def solution(name):
    answer = 0

    # 위아래 단순 계산
    updown = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    answer += sum(updown)

    # 연속하는 A 판단
    a_cnt = 0  # 'A'의 개수
    a_max = 0  # 'A'의 최대개수
    idx = 0  # 최대'A'개수 문자열의 마지막 인덱스
    a_startIdx = 0  # 최대'A'개수 문자열의 첫번째 인덱스
    wander_cnt = 0  # 좌우로 왔다갔다하는 횟수 카운트

    for i, n in enumerate(name):
        if n == 'A':  # 'A'개수의 최대값과 그 인덱스 계산
            a_cnt += 1
            if a_cnt > a_max:
                a_max = a_cnt
                idx = i
        else:
            a_cnt = 0
    # 최대'A'개수의 시작 인덱스
    a_startIdx = idx - a_max + 1

    # 최대'A'가 맨 앞이나 맨 끝에 있는 경우
    if a_startIdx == 0 or idx == len(name) - 1:
        answer += len(name) - 1 - a_max  # a_max개만큼 이동 안해도 됨
    else:
        left = len(name) - idx - 1  # 최대'A'뒤에 남아있는 문자의 개수
        if a_startIdx <= left:  # 뒤에 문자가 앞에 문자개수보다 많은 경우
            wander_cnt = (a_startIdx - 1) * 2 + left
        else:
            wander_cnt = (a_startIdx - 1) + left * 2 # 이해어렵...
        answer += min(wander_cnt, len(name) - 1)  # 그냥 한쪽방향으로 모두 이동하는 것과 비교

    return answer


if __name__ == '__main__':
    # name = 'KLDAJMAOKA'
    # name1 = "BBABAAAB"
    name2 = "AAABAAAAAB" # 반례
    print(solution(name2))
    # print(solution(name1))
    # print(solution(name2))

