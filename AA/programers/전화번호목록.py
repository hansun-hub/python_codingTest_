def solution(phone_book):
    hash_map={}
    for phone_num in phone_book:
        hash_map[phone_num]=1
    #print(hash_map)
    for phone_num in phone_book:
        jubdoo=""
        for number in phone_num:
            jubdoo+=number
            if jubdoo in hash_map and jubdoo != phone_num:
                return False
    return True
