import math
def solution(n):
    count = n
    for i in range(2, n+1):
        sqrti = int(math.ceil(math.sqrt(i)))
        for j in range(2, sqrti+1):
            if i % j == 0:   
                count -= 1
                break
    answer = count
    return answer