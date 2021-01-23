def solution(a, b):
    if a >= b :
        maxi = a
        mini = b
    else:
        maxi = b
        mini = a
    answer= 0
    for i in range(mini, maxi+1):
        answer += i
    return answer