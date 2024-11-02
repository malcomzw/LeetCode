class Solution:
    def trap(self, height: List[int]) -> int:
       

        #initialize 2 pointers left and right 
        #initialize left max and right max heights 
        left, right = 0 , len(height) - 1 
        left_max, right_max = 0, 0 
        water_trapped = 0

        # move the pointers towards each other 
        while left < right:
            #update the maxes 
            if height[left] < height[right] :
                #update the left max
                left_max = max(left_max, height[left])
                # calculate water trapped 
                water_trapped += left_max - height[left]
                left+=1
            else :
                # if the right is smaller or equal , UPDATE 
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                right -=1
        return water_trapped