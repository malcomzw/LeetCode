class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
    result = []

    # Step 2: Loop through each number as the fixed element
    for i in range(len(nums) - 2):
        # Skip duplicate elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Step 3: Set up two pointers
        left, right = i + 1, len(nums) - 1

        # Step 4: Move the two pointers to find valid triplets
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Move both pointers to skip duplicates for `left` and `right`
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < 0:
                # Move `left` pointer to increase the sum
                left += 1
            else:
                # Move `right` pointer to decrease the sum
                right -= 1

            return result  # Ensure this return statement is aligned within the function
        