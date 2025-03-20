# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p1,p2 = 0,0

        players.sort(), trainers.sort()

        count = 0

        while p1 < len(players) and p2 < len(trainers):
            if players[p1] < trainers[p2] or players[p1] == trainers[p2]:
                count+=1
                p1+=1
                p2+=1
            else:
                p2+=1
        
        return count
