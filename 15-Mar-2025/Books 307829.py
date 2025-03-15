# Problem: Books - https://codeforces.com/contest/279/problem/B


n, t = list(map(int, input().split()))
# n,t = 4, 5

a = list(map(int, input().split()))
# a = [3,1,2,1]


l = 0
max_books = 0
current_sum = 0
for right in range(len(a)):
    current_sum +=a[right]

    while current_sum > t:
        current_sum -= a[l]
        l+=1

    max_books = max(max_books, right-l+1)

print(max_books)

