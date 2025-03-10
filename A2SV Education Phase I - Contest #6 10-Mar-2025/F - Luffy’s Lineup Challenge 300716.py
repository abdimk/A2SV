# Problem: F - Luffy’s Lineup Challenge - https://codeforces.com/gym/594356/problem/F

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

swaps = []


for i in range(n):
    for j in range(n - 1):
        if b[j] > b[j + 1]: 
            b[j], b[j + 1] = b[j + 1], b[j]
            swaps.append((j + 1, j + 2)) 

        if b == a: 
            print(len(swaps))
            for x, y in swaps:
                print(x, y)
            exit()

print(len(swaps))
for x, y in swaps:
    print(x, y)
