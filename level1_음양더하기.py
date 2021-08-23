def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == False :
            answer -= absolutes[i]
        else : #if signs[i]:
            answer += absolutes[i]
    return answer

#enumerate, zip