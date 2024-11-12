class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #variables 
        #max sub array 
        maxSub =nums[0] #it cannot be zero there are vnegative values included
        curSum = 0

        #iterate the array 
        for num in nums:
            if curSum <0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub 
