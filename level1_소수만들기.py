import math
def solution(nums):
    count = 0
    for i in nums :
        for j in nums:
            for k in nums:
                if i!=j and j!=k and k!=i :
                    if isPrime(i+j+k) : 
                        count += 1
    return count / 6

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    return True

##다른 사람의 풀이
# def solution(nums):
#     from itertools import combinations as cb
#     answer = 0
#     for a in cb(nums, 3):
#         cand = sum(a)
#         for j in range(2, cand):
#             if cand%j==0:
#                 break
#         else:
#             answer += 1
#     return answer