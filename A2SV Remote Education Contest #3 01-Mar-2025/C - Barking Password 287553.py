# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

password = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]


if password in words:
    print("YES")
else:
    first_half = False
    second_half = False
    
    for word in words:
        if word[1] == password[0]:
            first_half = True
        if word[0] == password[1]:
            second_half = True
        
        if first_half and second_half:
            print("YES")
            break
    else:
        print("NO")