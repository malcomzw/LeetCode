class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hashmap to store the current window values 
        count ={}

        #left pointer 
        left = 0

        #max value result res
        result = 0

        #iterate the string with the right pointer
        for right in range(len(s)):
            #update the character counter for the current vallues in the window by one and the current value if not applicable , return 0 
            count[s[right]] = 1 + count.get(s[right], 0)

            #check if the window is valid 
            if (right - left + 1) - max(count.values()) > k:
                #reduce thewindow size 
                count[s[left]] -= 1
                left += 1

            result = max(result ,right - left + 1 )

        return result

