class Solution:
    def maxArea(self, height: List[int]) -> int:
        #initialize 2 pointers for the containers 
        left, right = 0 , len(height)-1 

        #initialize the maximum area to zero
        max_area = 0

        #loop until they meet 
        while left < right : 
            # calculate the current area 
            current_area= min(height[left], height[right]) * (right - left)

            #UPDATE if we find a larger max area 
            if current_area > max_area :
                max_area = current_area

        #Move the pointer on the least height 
            if height[left] < height[right] :
                left +=1
            else :
                height[right] < height[left]
                right -=1
        return max_area 