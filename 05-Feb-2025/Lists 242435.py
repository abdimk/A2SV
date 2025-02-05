# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    
    result = []

    for _ in range(N):
        command = input()
        option = command.split()
        
        if option[0] == "insert":
            position, value = option[1], option[-1]
            result.insert(int(position), int(value))
            
        if option[0] == "print":
            print(result)
            
        if option[0] == "append":
            value = option[1]
            result.append(int(value))
            
        if option[0] == "sort":
            result.sort()
            
        if option[0] == "reverse":
            result.reverse()
            
        if option[0] == "pop":
            result.pop()
            
        if option[0] == "remove":
            value = option[-1]
            result.remove(int(value))
         