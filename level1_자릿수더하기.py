def solution(n):
    answer = 0
    s = str(n)
    end = len(s)
    for i in range(0, end):
        answer += int(s[i])
    return answer