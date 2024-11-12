class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #declare the set to store the current window elements 
        char_set = set()

        #declare pointer and max length 
        left = 0 
        max_len = 0 

        #iterate over the string with the right pointer 
        for right in range(len(s)) :
            # check if there are duplicates 
            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1 
            
            #add the current element to the charset 
            char_set.add(s[right])

            #calculate the lenght of the max len 
            max_len = max(max_len , right - left + 1)
        return max_len 



        