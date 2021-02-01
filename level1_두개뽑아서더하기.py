def solution(numbers):
    end = len(numbers)
    add = 0
    answer = []
    for i in range(0, end):
        for j in range(i+1, end):
            add = numbers[i] + numbers[j]
            answer.append(add)
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer