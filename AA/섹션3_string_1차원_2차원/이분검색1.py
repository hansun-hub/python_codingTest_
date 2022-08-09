n, m = map(int, input().split());
arr = list(map(int, input().split()));
s = 0; # 시작점
e = n; # 끝점


arr.sort(); # 오름차순 정렬

while s <= e: # 이분 탐색
    mid = (s + e) // 2; # 중간점
    if arr[mid] == m: # 목표값 찾은 경우 탐색 완료
        print(mid + 1);
        break;
    elif arr[mid] < m : # 중간점보다 목표값이 큰 경우
        s = mid + 1;
    elif arr[mid] > m : # 중간점보다 목표값이 작은 경우   
        e = mid - 1;
