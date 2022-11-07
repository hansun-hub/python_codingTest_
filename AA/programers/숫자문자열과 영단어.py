def solution(s):
    dict={}
    en=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        dict[en[i]]=i
    print(dict)
    #딕셔너리에 키와 값으로 넣어주었다
    result=''
    eng=''
    for i in s: #문자열 하나씩 확인
        if i.isdigit():
            result = result+i
        elif i.isalpha(): #문자면 치환작업
            eng=eng+i
            if eng in dict.keys(): #이어붙이다가 숫자단어가 되면
                result = result+str(dict[eng])
                eng='' #하나씩 이어붙이는 걸 다시 새로 시작할 수 있도록 초기화
    
    
    return int(result)
