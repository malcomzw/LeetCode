class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       #we calculate the prefix and the suffix 
        n = len(nums)
        result = [1] * n
        #compute left products  
        #initially set the prefix to 1 
        prefix = 1
        #iterate the given array to the end calculating the prefix 
        for i in range(n):
            result[i] = prefix 
            # multiply with the prefix and update 
            prefix *= nums[i] #update the multiplication by current i [i]
            
        #calculate into the suffix from the back 
        suffix=1
        for i in range(n-1,-1,-1) :
             #traverse from the end
             result[i] *= suffix 
             suffix *= nums[i]
        return result 

            