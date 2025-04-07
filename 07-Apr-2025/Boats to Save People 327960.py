# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort() # for easier finding
        left, right = 0, len(people) - 1
        boats = 0 
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats += 1
            else : # otherwise, the person will have to have their own life boat
                right -= 1
                boats += 1
        return boats