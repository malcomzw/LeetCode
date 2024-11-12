class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #variables 
        #left pointer to the beginning of the array 
        left = 0
        #current_sum of the window 
        current_sum = 0
        #size of the minimum sub array 
        min_len = float('inf')

        #operations 
        #iterate the array with the right pointer 
        for right in range(len(nums)):
            #add the current iterated value to the sum 
            current_sum += nums[right]

            #check to see if the values compute to the target 
            while current_sum >= target:
                min_len =min(min_len, right - left + 1 )
                current_sum -=nums[left]
                left +=1 

        return 0 if min_len == float('inf') else min_len


