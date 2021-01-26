def solution(arr1, arr2):
    answer = [[]]
    answer.remove([])
    single_lst = []
    end1 = len(arr1)
    end2 = len(arr1[0])
    for i in range(0, end1):
        for j in range(0, end2):
            ij = (arr1[i])[j] + (arr2[i])[j]
            single_lst.append(ij)
        answer.insert(i, single_lst)
        single_lst = []
    return answer