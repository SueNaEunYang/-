import math
def solution(s):
    length = int(len(str(s)))
    print(length)
    if length % 2 == 0:
        mid = int(length / 2)
        answer = s[mid-1:mid+1]
        # print(mid)
        # print(answer)
    else:
        mid = int(math.ceil(length/2))
        answer = s[mid-1:mid]
        # print(mid)
        # print(answer)
    return answer

#test case
solution("solution")
solution("qwert")