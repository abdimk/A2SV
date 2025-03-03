# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        
        for row in image:
            
            flipped_row = row[::-1]
            
            
            inverted_row = [num ^ 1 for num in flipped_row]
            
            
            result.append(inverted_row)
        
        return result
        