class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize left and right pointer at the second index 
        # traverse the array , updating the left pointer after every unique element
        l = 1

        for r in range (1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l