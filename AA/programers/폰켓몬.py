def solution(nums):
    l=len(nums)//2
    map={}
    
    for i in nums:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    if l<len(map.keys()):
        return l
    else:
        return len(map.keys())
            
    return answer
