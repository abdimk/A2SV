# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:

    # the key is use manhatten distance formula between you and the target 
    # also the each ghosts and the target 
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        your_distance = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            g_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])

            if g_distance <= your_distance:
                return False
        return True