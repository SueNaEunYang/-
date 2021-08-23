#월간 코드 챌린지 시즌1
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer = answer + a[i]*b[i]
    return answer


## zip을 사용한 풀이 -
# def solution(a, b):
#     return sum([x*y for x, y in zip(a,b)])