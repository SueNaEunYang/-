def solution(phone_number):
    end = int(len(phone_number))
    print("*" * (end-4) + phone_number[end-4:])
    return "*" * (end-4) + phone_number[end-4:]


#replace
# def solution(phone_number):
#     end = int(len(phone_number))
#     for i in range(0, end-4):
#         phone_number = phone_number.replace(phone_number[i], "*")
#     return phone_number

# test case
solution("01012341234")
solution("0212341234")