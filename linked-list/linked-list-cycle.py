# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head ,head

        while fast and fast.next:

        # move the pointers at tdifferent speeds 
            slow = slow.next 
            fast = fast.next.next 

        #if they meet there is a cycle 
            if    fast == slow :
                return True      