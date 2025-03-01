# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

t = int(input().strip())

def generate_matrix(n):
    if n == 2:
        return -1  
    
    matrix = [[0] * n for _ in range(n)]
    
    numbers = list(range(1, n * n + 1))
    odd_numbers = numbers[::2]  
    even_numbers = numbers[1::2]  
    
    fill_order = odd_numbers + even_numbers  
    
    index = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = fill_order[index]
            index += 1
    
    return matrix

for _ in range(t):
    n = int(input().strip())
    result = generate_matrix(n)
    
    if result == -1:
        print(-1)
    else:
        for row in result:
            print(" ".join(map(str, row)))
