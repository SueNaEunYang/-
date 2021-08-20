def solution(scores):
    # import numpy as np
    # np.transpose(scores)
    transpose_scores = []
    for i in range(len(scores)):
        transpose_row = []
        for j in range(len(scores[i])):
            transpose_row.append(0)
        transpose_scores.append(transpose_row)
    
    for i in range(len(scores)):
        for j in range(len(scores[i])):
            transpose_scores[i][j] = scores[j][i]
    scores = transpose_scores

    average = []
    avg = 0
    num = []
    grade = ""
 
    for i in range(len(scores)):
        is_unique = True
        if scores[i][i] == min(scores[i]) or scores[i][i] == max(scores[i]):
            for j in range(len(scores[i])):     
                if j != i :
                    if scores[i][j] == scores[i][i]:
                        is_unique = False
                    else:
                         pass
                else:
                    pass
            if is_unique == True :
                scores[i][i] = 0
                num.append(1)
            else :
                num.append(0)
        else: 
            num.append(0)
            
        avg = sum(scores[i]) / (len(scores[i]) - num[i])
        average.append(avg)
            
    for i in range(len(average)):
        if average[i] >= 90 :
            grade = grade + "A"
        elif average[i] >= 80 :
            grade = grade + "B"
        elif average[i] >= 70 :
            grade = grade + "C"
        elif average[i] >= 50 :
            grade = grade + "D"
        else:
            grade = grade + "F"
    print(grade)
    return grade

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])

# 파이썬은 zip, enumerate, counter, join 등 손쉬운 함수들을 사용하면 더 짧게 짤 수 있었당!! 갈 길이 멀다 ㅠ.ㅠ

