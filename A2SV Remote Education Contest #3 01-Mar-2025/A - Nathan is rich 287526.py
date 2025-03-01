# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

t = int(input())
 
for i in range(t):
    n = int(input())
    print(n // 4 + (1 if n % 4 != 0 else 0))