def solution(s):
    length = int(len(s))
    answer = True
    if length == 4 or length == 6:
        answer = s.isdigit()
    else:
        answer = False
    return answer