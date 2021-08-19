# 내 코드는 너무 스레기야 슬퍼 ㅠㅠ

def solution(s):
    s= s.replace("zero","0")
    s= s.replace("one","1")
    s= s.replace("two","2")
    s= s.replace("three","3")
    s= s.replace("four","4")
    s= s.replace("five","5")
    s= s.replace("six","6")
    s= s.replace("seven","7")
    s= s.replace("eight","8")
    s= s.replace("nine","9")
    
    return int (s)


def what_I_actually_wanted_to_do(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(nums)):
        s = s.replace(nums[i], str(i))

    return int(s)


# 노가다 본능으로 회귀해서 멈춤
#    
    # lst = []
    # listLength = len(lst)
    # det = ["zer", "one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
    # index = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # marking = 0
    # stringLength = len(s)
    # for i in (marking, stringLength):
    #     if s[marking].isdigit() == True :
    #         lst.append(s[marking])
    #         marking = marking +1
    #     else :
    #         lst.append = det.index(s[marking:marking + 2])
    #             if lst[-1] = 0 :
    #                 s[marking +3] = ""
    #             elif lst[-1] = 3 :
    #                 s[marking +3] = ""
    #                 s[marking +4] = ""



            # lst.append(index.index(s[marking:markingend]))
    # for i in (0,listLength) :
    #     answer = answer + "lst"
    # 
    # return answer