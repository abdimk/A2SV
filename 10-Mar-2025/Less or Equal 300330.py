# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n,k = list(map(int, input().split()))


arr = list(map(int, input().split()))
arr.sort()


if k == 0:
    if arr[0] > 1:
        print(arr[0]-1)
    else:
        print(-1)
else:
    elem = arr[k-1]
    count = len([i for i in arr if i <= elem])

    if count == k:
        print(elem+1)
    else:
        print(-1)