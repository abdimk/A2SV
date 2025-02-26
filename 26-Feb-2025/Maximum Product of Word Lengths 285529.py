# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bit_masks = [0] * n  
        lengths = [len(word) for word in words]  
        
        
        for i, word in enumerate(words):
            for char in word:
                bit_masks[i] |= (1 << (ord(char) - ord('a')))
        
        max_product = 0
        
        
        for i in range(n):
            for j in range(i + 1, n):
                if bit_masks[i] & bit_masks[j] == 0:  
                    max_product = max(max_product, lengths[i] * lengths[j])
        
        return max_product
