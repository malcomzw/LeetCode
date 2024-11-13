# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.

        # Step 1: Use Floyd's Tortoise and Hare algorithm to detect a cycle.
        slow = fast = head
        
        # Move slow by 1 step and fast by 2 steps.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast meet, there's a cycle.
            if slow == fast:
                # Step 2: Find the entry point of the cycle.
                # Move slow to the head.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # This is the starting node of the cycle
        
        # No cycle found
        return None
