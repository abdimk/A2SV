# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    result = ""
    
    for i in s:
        if i.islower():
            result+=i.upper()
        if i.isupper():
            result+=i.lower()
        if not i.islower() and not i.isupper():
            result+=i
    
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)