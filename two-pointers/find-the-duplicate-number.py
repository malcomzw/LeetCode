class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
    
    while True:
        slow = nums[slow]       # Move slow by 1 step
        fast = nums[nums[fast]] # Move fast by 2 steps
        if slow == fast:        # They meet inside the cycle
            break

    # Phase 2: Finding the entrance to the cycle (the duplicate)
    slow = nums[0]  # Reset slow to the start
    while slow != fast:  # Move both pointers until they meet again
        slow = nums[slow]
        fast = nums[fast]

    return slow  # This is the duplicate number