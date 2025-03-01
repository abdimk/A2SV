# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

def can_survive(n, k, healths, positions):
    zombies = list(zip(healths, positions))
   
    zombies.sort(key=lambda x: abs(x[1]))
    
   
    time_left = [abs(pos) for _, pos in zombies]  
    healths_sorted = [h for h, _ in zombies]  
    
   
    current_time = 0
    bullets_used = 0
    
    for i in range(n):
        time_to_reach = time_left[i]
        health = healths_sorted[i]
        
    
        if health > time_to_reach:
            return "NO"        
      
        bullets_used += health
        if bullets_used > k * current_time:  
            return "NO"
        
    return "YES"


t = int(input(":"))
for _ in range(t):
    n, k = map(int, input().split())
    healths = list(map(int, input().split()))
    positions = list(map(int, input().split()))
    print(can_survive(n, k, healths, positions)) 
