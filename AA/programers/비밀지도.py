def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n): #한변의 크기 만큼 반복해요
        tmp=bin(arr2[i] | arr1[i])
        # print(tmp)
        tmp=tmp[2:].zfill(n)
        #print(tmp)
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    return answer
