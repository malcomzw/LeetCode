class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        # Edge case 1: If the list is empty, return 0
        if not nums:
            return 0
        
        # Edge case 2: If the list has 1 or fewer elements, return the length of the list
        if len(nums) <= 2:
            return len(nums)

        l, r = 0, 0  # Two pointers: l for the last valid index, r for the current index

        while r < len(nums):  # Iterate until r reaches the end of the array
            count = 1  # We start counting duplicates from the current element (nums[r])
            
            # Count the number of occurrences of nums[r]
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1  # Move r forward while we find duplicates
                count += 1  # Increase count for duplicates

            # Place at most 2 of the duplicate numbers in the valid positions
            for i in range(min(2, count)):
                nums[l] = nums[r]  # Assign the current element at position l
                l += 1  # Move l to the next valid position
            
            r += 1  # Move r to the next element to process
        
        return l  # Return the length of the modified array
