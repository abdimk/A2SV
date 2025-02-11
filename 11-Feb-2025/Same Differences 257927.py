# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

import sys

input = sys.stdin.read
def solve():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = map(int, data[index:index + n])
        index += n
        
        res = 0
        freq = {}
        
        for i, v in enumerate(arr):
            key = v - i
            
