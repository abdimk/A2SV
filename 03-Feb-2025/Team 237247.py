# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())

solved = 0

for _ in range(n):

    a,b,c = map(int, input().split())
    if a + b + c >= 2:
        solved+=1

print(solved)

