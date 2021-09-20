def solution(lottos, win_nums):
    numZero = 0
    numWin = 0
    for i in lottos :
        if i == 0 :
            numZero += 1
        if i in win_nums :
            numWin += 1
    return [rank(numWin+numZero), rank(numWin)]

def rank(num):
    if num == 0 :
        return 6
    else :
        return 7 - num