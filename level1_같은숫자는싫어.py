def solution(arr):
    answer=[]
    arr.append(100)
    for i in range(len(arr)):
        if arr[i]==100:
            if arr[i-1] != arr[i-2]:
                arr.append(arr[i-1])
            else : 
                break
        elif arr[i] != arr[i+1] :
            answer.append(arr[i])
        else :
            pass
    return answer

## 다른 풀이(1)
# return [s[i] for i in range(len(s)) if s[i] != s[i+1:i+2]]

## 다른풀이(2)
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a
