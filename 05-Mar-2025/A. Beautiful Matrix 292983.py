# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A


matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)


for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_pos = i + 1  # Convert to 1-based index
            col_pos = j + 1  # Convert to 1-based index
            break

moves = abs(row_pos - 3) + abs(col_pos - 3)
print(moves)
