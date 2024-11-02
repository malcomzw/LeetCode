class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        #sort the array nums 
        nums.sort()

        #closest sum to inifinity
        closest_sum = float('inf')

        #iterate through the array treating aech number like the first of the triplets 
        for i in range (len(nums) -2 ):

            #initialize 2 pointers 
            l,r = i+1 , len(nums)-1

            while l < r :
                # calculate the current sum of the triplet 
                current_sum = nums[i] + nums[l] + nums[r]

                #  compare the value with the current closest sum 
                if  abs(current_sum- target) < abs(closest_sum - target):
                    closest_sum = current_sum 

                #move the pointers 
                if current_sum < target:
                    l +=1
                elif current_sum > target:
                    r-=1
                else :
                    return current_sum
        return closest_sum 






