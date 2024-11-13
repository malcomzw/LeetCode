class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #variables 
        left = 0
        zero_count = 0  #track the zeros 
        max_len = 0 #LONGEST  sub array track 

        #operations 
        #iterate the array with the right pointer 
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count +=1 
            
            while zero_count> k:
                if nums[left] == 0:
                    zero_count -= 1
                left +=1
            #update the max lenght 
            max_len = max(max_len , right - left + 1)
        return max_len