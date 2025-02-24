# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0

        for n, v in count.items():
            group_size = n + 1
            group_needed = (n + v) // group_size
            res+=group_size * group_needed

        return res