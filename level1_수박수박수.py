
import math
def solution(n):
    nn = math.floor(n/2)
    if n % 2 == 0:
        answer = "수박" * int(nn)
    else:
        answer = "수박" * int(nn) + "수"
    return answer

# solution(4)
# solution(7)