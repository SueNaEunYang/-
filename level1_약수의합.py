def solution(n):
    tot = n
    for i in range(1,n):
        if n % i == 0:
            tot += i
    return tot