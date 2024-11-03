# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast , slow = head , head 

        while fast and fast.next:  #not out of bounce 
            #iterayte the fast pointer to the end 
            slow = slow.next 
            fast = fast.next.next

        return slow 