class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #check if 1 not present 
        if not nums or 1 not in nums :
            return 1

        #replace all the numberrs out of range 
        for i ,num in enumerate(nums) :
            if num <= 0 or num> len(nums):
                nums[i] =1

        #use negative to mark seen values \
        for num in nums :
            if abs(num) <= len(nums) :
                nums[abs(num)-1] = -abs(nums[abs(num)-1])            

        #check for the first positive value 
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        #return the next value if none found 
        return len(nums) +1
