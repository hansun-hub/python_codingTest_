def solution(s):
    answer = []
    s=s[2:-2]
    s=s.split("},{")
    #print(s)
    s.sort(key=len)
    #print(s)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
                              
    return answer
