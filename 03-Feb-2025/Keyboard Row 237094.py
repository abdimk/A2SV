# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []

        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for word in words:

            word_set = set(word.lower())

            if word_set <= row1 or word_set <= row2 or word_set <= row3:
                result.append(word)

        return result