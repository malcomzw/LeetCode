class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        result = 0

        for c in s :
            if c in seen :
                seen.remove(c)
                result +=2 
            else :
                seen.add(c)

        return result +1 if seen else result