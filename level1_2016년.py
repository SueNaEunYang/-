def solution(a, b):
    c = 5
    if a == 1 :
        c = c + b
    elif a == 2 :
        c = c + 31 +b
    elif a == 3 :
        c = c + 31+29 +b
    elif a == 4 :
        c = c + 31+29+31 +b
    elif a == 5 :
        c = c + 31+29+31+30 +b
    elif a == 6 :
        c = c + 31+29+31+30+31 +b
    elif a == 7 :
        c = c + 31+29+31+30+31+30 +b
    elif a == 8 :
        c = c + 31+29+31+30+31+30+31 +b
    elif a == 9 :
        c = c + 31+29+31+30+31+30+31+31 +b
    elif a == 10 :
        c = c + 31+29+31+30+31+30+31+31+30 +b
    elif a == 11 :
        c = c + 31+29+31+30+31+30+31+31+30+31 +b
    else:
        c = c + 31+29+31+30+31+30+31+31+30+31+30 +b
    
    mod = c%7
    if mod == 1 :
        answer = "SUN"
    elif mod == 2 :
        answer = "MON"
    elif mod == 3 :
        answer = "TUE"
    elif mod == 4 :
        answer = "WED"
    elif mod == 5 :
        answer = "THU"
    elif mod == 6 :
        answer = "FRI"
    else:
        answer = "SAT"
        
    return answer