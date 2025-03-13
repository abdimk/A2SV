# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        # group length 1 => append to s
        # append the char to the group length
        r , l = 0,0   # r = write , #l = read
        n = len(chars)
        while l < n:
            char = chars[l]
            count = 0

            while l < n and chars[l] == char:
                l+=1
                count+=1

            chars[r] = char
            r+=1

            if count > 1:
                for digit in str(count):
                    chars[r] = digit
                    r+=1

        return r