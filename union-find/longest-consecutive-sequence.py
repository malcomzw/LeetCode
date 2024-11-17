class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert the array into set 
        numSet = set(nums)
        longest = 0 

        #iterate all the numbers in the set 
        #check if the current number is beginning of sequence 
        for num in numSet:
            if num -1 not in numSet:
                current_length = 1

                #increment the sequence 
                while num + current_length in numSet:
                    current_length += 1
                longest = max(longest, current_length)
        return longest 