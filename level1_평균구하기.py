def solution(arr):
    sum = 0
    end = int(len(arr))
    for i in range(0, end):
        sum += arr[i]
    return sum / (end)