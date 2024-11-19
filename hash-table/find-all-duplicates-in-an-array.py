class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        duplicates = [] #declare duplicates 

        #visit the given array 
        for num in nums: 
            #iterate to check and operate 
            index = abs(num) - 1 #map to index 
            if nums[index] <0:
                #iif the value at index is <0
                duplicates.append(abs(num))
            else :
                nums[index] = -nums[index]
        return duplicates

