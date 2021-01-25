def solution(num):
    step = 0
    answer = -1
    while step <= 500 :
        if num == 1:
            answer = step
            break
        elif num % 2 == 0:
            num = num / 2
            step += 1
        else:
            num = num * 3 + 1
            step += 1
    return answer